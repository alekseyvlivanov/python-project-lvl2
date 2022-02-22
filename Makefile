install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff

test-coverage-cc:
	poetry run pytest --cov=gendiff --cov-report xml

selfcheck:
	poetry check

check: selfcheck lint test

build: check
	poetry build

publish: check
	poetry publish --dry-run

package-install: check
	python3 -m pip install --force-reinstall --user dist/*.whl

.PHONY: install lint build publish package-install
