venv_name = .venv

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

build-env: ## Build virtual environment and install required packages
	sudo apt-get install gnome-screensaver xdotool
	virtualenv -p python3 $(venv_name)
	$(venv_name)/bin/pip3 install -Ur requirements.txt

app: ## Run the application
	. $(venv_name)/bin/activate; \
	python3 main.py

generate-data:  ## Generate faces for your face recognition algorithm
	. $(venv_name)/bin/activate; \
	python3 src/generate_data.py

format-code:  ## Sort import statements in the right format ; Reformat code to be PEP8-aligned
	isort .; autopep8 --in-place -r src

update-reqs: ## Update requirements file
	$(venv_name)/bin/pip3 freeze > requirements.txt
