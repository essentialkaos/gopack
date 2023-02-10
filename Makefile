########################################################################################

.DEFAULT_GOAL := help
.PHONY = install uninstall get-shellcheck test help

########################################################################################

get-shellcheck: ## Download and install the latest version of shellcheck (requires sudo)
ifneq ($(shell id -u), 0)
	@echo -e "\e[31m▲ This target requires sudo\e[0m"
	@exit 1
endif

	@echo -e "\e[1;36;49m\nDownloading shellcheck…\n\e[0m"
	curl -#L -o shellcheck-latest.linux.x86_64.tar.xz https://github.com/koalaman/shellcheck/releases/download/latest/shellcheck-latest.linux.x86_64.tar.xz
	tar xf shellcheck-latest.linux.x86_64.tar.xz
	rm -f shellcheck-latest.linux.x86_64.tar.xz
	cp shellcheck-latest/shellcheck /usr/bin/shellcheck || :
	rm -rf shellcheck-latest

	@echo -e "\e[1;32;49m\nShellcheck successfully downloaded and installed!\n\e[0m"

test: ## Run shellcheck tests
	shellcheck SOURCES/gopack SOURCES/gopack-build

install: ## Install app to current system (requires sudo)
ifneq ($(shell id -u), 0)
	@echo -e "\e[31m▲ This target requires sudo\e[0m"
	@exit 1
endif

	@echo -e "\e[1;36;49m\nInstalling app…\n\e[0m"
	install -pm 755 SOURCES/gopack /usr/bin/
	install -pm 755 SOURCES/gopack-build /usr/bin/

	@echo -e "\e[1;32;49m\nApp successfully installed!\n\e[0m"

uninstall: ## Uninstall app from current system (requires sudo)
ifneq ($(shell id -u), 0)
	@echo -e "\e[31m▲ This target requires sudo\e[0m"
	@exit 1
endif

	@echo -e "\e[1;36;49m\nUninstalling app…\n\e[0m"
	rm -f /usr/bin/gopack || :
	rm -f /usr/bin/gopack-build || :

	@echo -e "\e[1;32;49m\nApp successfully uninstalled!\n\e[0m"

help: ## Show this info
	@echo -e '\nSupported targets:\n'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[33m%-19s\033[0m %s\n", $$1, $$2}'
	@echo -e ''

################################################################################
