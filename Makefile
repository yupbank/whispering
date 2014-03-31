deps:
	pip install -r pip-req.txt

.PHONY: pep8
pep8:
	@flake8 server --ignore=F403,F401
