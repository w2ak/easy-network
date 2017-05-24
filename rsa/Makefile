.PHONY: all download wipe bootstrap
TGZURL:="https://github.com/OpenVPN/easy-rsa/releases/download/3.0.1/EasyRSA-3.0.1.tgz"
TGZSUM:="d20f646e33ec803444dfcd446553f1d6001227fedec93280c212b34cccee11b184599f1b2ae6a3ce9cf6c9ac52f2b840ebb645536df6ddf55382fa25c22df81f"
TGZDIR:="EasyRSA-3.0.1"

all:

bootstrap: .bootstrap.ok

.bootstrap.ok: .download.ok .config.ok
	@cat $< > $@

download: .download.ok

.download.ok:
	@./download "$(TGZURL)" "$(TGZSUM)" "$(TGZDIR)"
	@test -f $@

config: .config.ok

.config.ok: .download.ok
	@./config
	@test -f @

wipe:
	@rm -f .download.ok
	@rm -rf easy-rsa
