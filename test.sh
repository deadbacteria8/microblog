#!/bin/sh

source .venv/bin/activate
flask db upgrade
make test
