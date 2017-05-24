.PHONY: help bootstrap wipe release test/% configfile install

help:
	@echo "Accessible rules :\n"
	@echo "  help          Show this help."
	@echo "  bootstrap     Install dependencies, setup environment."
	@echo "  wipe          Clean everything."
	@echo "  release       Create release tarball."
	@echo "  install       Install easy-network after configuration."
	@echo "  test/*        Launch a test."

bootstrap: .bootstrap.ok

.bootstrap.ok:
	@./bootstrap
	@test -f $@

rsa/.download.ok:
	@make -C rsa download

vpn/.install.ok:
	@make -C vpn install

wipe:
	@rm -f .bootstrap.ok
	@make -C rsa wipe

release:
	@mkdir -p release
	@tar -X .releaseignore -czf release/easy-network.tgz .

test/%: release
	@[ -d $@ ] && cd $@ && vagrant up

configfile: config.js

config.js: .bootstrap.ok
	@./env2config $<
	@test -f $@

install: configfile
	@./install
