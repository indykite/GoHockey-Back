#!/bin/sh
export FLASK_APP=./GoGretzky/src/route.py
pipenv run flask --debug run -h 0.0.0.0
