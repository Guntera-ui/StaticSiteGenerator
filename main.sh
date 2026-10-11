#!/usr/bin/env zsh

set -e

python3 src/main.py
cd docs
python3 -m http.server 8888
