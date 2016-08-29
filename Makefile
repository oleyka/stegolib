VERSION=$(/usr/bin/env python setup.py --version)

default: test

setup:
	virtualenv venv
	. venv/bin/activate  ## && pip install -r requirements.txt

package: setup
	@python setup.py sdist

test: setup
	@python setup.py pytest

clean:
	@find . -name \*.pyc -exec rm -v '{}' +
	@find . -name __pycache__ -prune -exec rm -vfr '{}' +
	@find . -name .cache -prune -exec rm -vfr '{}' +
	@rm -rf build bdist cover dist sdist
	@rm -rf .tox .eggs
	@rm -rf distribute-* *.egg *.egg-info

.PHONY: default setup tox clean
