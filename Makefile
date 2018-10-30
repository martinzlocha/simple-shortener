ifeq ($(OS),Windows_NT)
   VENV_BIN = venv/Scripts
else
   VENV_BIN = venv/bin
endif

all: run

clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf *.log*

venv:
	virtualenv --python=python3 venv && $(VENV_BIN)/python setup.py develop

run: venv
	FLASK_APP=simple_shortener SIMPLE_SHORTENER_SETTINGS=../settings.cfg $(VENV_BIN)/flask run

test: venv
	SIMPLE_SHORTENER_SETTINGS=../settings.cfg $(VENV_BIN)/python -m unittest discover -s tests

sdist: venv test
	$(VENV_BIN)/python setup.py sdist
