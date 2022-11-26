.PHONY: help
help:	### Display all available commands
ifeq ($(UNAME), Linux)
	@grep -P '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
else
	@# this is not tested, but prepared in advance for you, Mac drivers
	@awk -F ':.*###' '$$0 ~ FS {printf "%15s%s\n", $$1 ":", $$2}' \
		$(MAKEFILE_LIST) | grep -v '@awk' | sort
endif

# Targets
#
.PHONY: install
install: ### Set up local environment (linux / OSX)
	python3 -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install -Ur dev-requirements.txt
	. venv/bin/activate && pre-commit install 