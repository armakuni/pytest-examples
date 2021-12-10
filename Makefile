test:
	PYTHONPATH=. pytest tests

fmt:
	black .

lint:
	flake8 .