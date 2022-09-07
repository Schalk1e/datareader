.PHONY: doc

doc:
	python3 -m pydoc -w src/ && mv *.html doc

lint: 
	sh .ci/lint.sh