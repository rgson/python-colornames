#!/usr/bin/make -f


.PHONY: all
all: clean test build


.PHONY: build
build:
	python3 -m build


.PHONY: clean
clean:
	rm -rf dist *.egg-info


.PHONY: test
test:
	python3 -m unittest tests
