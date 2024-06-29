#!/bin/zsh
parallel -i docker run --rm -v.:/a 'python:3.{}-slim' /a/tests.py -- {4..12}
