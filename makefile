setup:
	python -m pip install --upgrade pip
	pip install pytest

test:
	pytest -q

spec-check:
	@echo "spec-check placeholder: verify implementation aligns with specs/"
