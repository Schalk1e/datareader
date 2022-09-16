include .venv/env

.PHONY: doc

doc:
	pdoc -o ./doc src/datareader

lint: 
	sh .ci/lint.sh