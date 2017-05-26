def __ns2cnf (namespace):
    cnf = dict()
    ns = vars(namespace)
    return cnf

class VpnConfigError(Exception): pass
class VpnConfigMissing(Exception): pass

class VpnConfigValues:
    _checkers = dict()
    _defaults = dict()
    _keys = dict()

    @classmethod
    def defaults(cls):
        for k in cls._defaults:
            yield(k,cls._defaults[k])

    @classmethod
    def checkers(cls):
        for k in cls._checkers:
            yield cls._checkers[k]

    @classmethod
    def realname(cls, key):
        if key in cls._keys:
            return cls._keys[key]
        return key

def __vpn_cnf(required = True, default = None, choices = None, realname = None):
    def decorator(f):
        key = f.__name__
        def checker(config):
            if key in config:
                if choices is not None and config[key] not in choices:
                    raise VpnConfigError('"{:}" should be among ({:}).'.format(key, ','.join(choices)))
                return f(config=config, value=config[key])
            elif required:
                raise VpnConfigMissing('Missing config item "{:}".'.format(key))
        VpnConfigValues._keys[key] = key if realname is None else realname
        checker.__name__ = '{:}_checker'.format(key)
        VpnConfigValues._checkers[key] = checker
        if default is not None:
            VpnConfigValues._defaults[key] = default
        return None
    return decorator

@__vpn_cnf(realname='', default='server', choices=['server','client'])
def type(config, value=None):
    return 0

@__vpn_cnf(realname='dev-type', default='tun', choices=['tun','tap'])
def dev_type(config, value=None):
    return 0

@__vpn_cnf(default='udp', choices=['udp','tcp'])
def proto(config, value=None):
    return 0

class VpnConfig:
    def __init__(self, config = None):
        self.config = dict() if config is None else config

    @classmethod
    def fromNamespace(cls, ns):
        return cls(__ns2cnf(ns))

    @classmethod
    def default(cls):
        cnf = dict()
        for k,v in VpnConfigValues.defaults():
            cnf[k] = v
        return cls(cnf)

    def update(self, food):
        if isinstance(food, dict):
            for k in food:
                self.config[k] = food[k]
            return self
        if isinstance(food, list):
            for c in food:
                k,v = c
                self.config[k] = v
            return self
        if isinstance(food, VpnConfig):
            return self.update(food.config)
        return self.update(vars(food))

    def check(self):
        for ck in VpnConfigValues.checkers():
            try:
                ck(self.config)
            except VpnConfigError as vce:
                return 1,vce.args[0]
            except VpnConfigMissing as vcm:
                return 2,vcm.args[0]
        return 0, None

    def __toString(key, value):
        if key:
            if '\n' in value:
                return '<{0}>\n{1}\n</{0}>'.format(key, value)
            if ' ' in value:
                return "{0} '{1}'".format(key, value)
            return '{0} {1}'.format(key, value)
        return '{0}'.format(value)

    def __str__(self):
        res = list()
        for k in VpnConfigValues._keys:
            if k in self.config:
                val = self.config[k]
                key = VpnConfigValues._keys[k]
                res.append(VpnConfig.__toString(key,val))
        return '\n'.join(res)

if __name__=='__main__':
    c1 = VpnConfig.default()
    print(c1)
    print(c1.config)
    print(c1.check())

