PROJECT_DIR = ${PWD}

.PHONY: unit_tests
unit_tests: 
	export PYTHONPATH=${PROJECT_DIR} && cd tests && python3 -u tests.py