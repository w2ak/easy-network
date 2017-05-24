.PHONY: all install bootstrap

all:

bootstrap: .bootstrap.ok

.bootstrap.ok: .install.ok
	@cat $< > $@

install: .install.ok

.install.ok:
	@./install
	@test -f $@
