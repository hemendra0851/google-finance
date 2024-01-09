#!/bin/bash
pylint *.py */*.py --disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,useless-parent-delegation
pytest