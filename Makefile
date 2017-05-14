.PHONY: help bootstrap wipe

help:
	@echo "Accessible rules :\n"
	@echo "  help          Show this help."
	@echo "  bootstrap     Install dependencies, setup environment."
	@echo "  wipe          Clean everything."

bootstrap: .bootstrap.ok

.bootstrap.ok:
	@./bootstrap > $@

wipe:
	@rm -f .bootstrap.ok