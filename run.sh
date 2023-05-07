#!/bin/bash

python3 -m venv cram-env
source cram-env
pip3 install -r requirements.txt
python3 main.py