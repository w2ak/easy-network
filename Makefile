.PHONY: help bootstrap wipe release

help:
	@echo "Accessible rules :\n"
	@echo "  help          Show this help."
	@echo "  bootstrap     Install dependencies, setup environment."
	@echo "  wipe          Clean everything."
	@echo "  release       Create release tarball."

bootstrap: .bootstrap.ok

.bootstrap.ok:
	@./bootstrap
	@test -f $@

wipe:
	@rm -f .bootstrap.ok
	@make -C rsa wipe

release:
	@mkdir -p release
	@tar -X .releaseignore -czf release/easy-network.tgz .
