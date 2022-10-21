#!/bin/bash

# check if virtual environment exists and set up if it doesn't
[ ! -d "env" ] && python3 -m venv .env

# execute the following commands within the virtual environment
# i.e. install dependencies in virtual environment instead of globally on the executing system
source .env/bin/activate

# update pip in venv
python -m pip install --upgrade pip

# install requirements
pip install -r requirements.txt

# print package installations in env
echo # print newline
pip freeze
