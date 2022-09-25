#!/bin/bash

clear

if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, check out https://installpython3.com/' >&2
  exit 1
fi

if ! [[ -x "$(command -v pip3)" ]]
then
  echo 'Error: 
    This program requires pip3 to install dependencies, but it looks like pip3 is not installed.
    To install, check out https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3' >&2
  exit 1
fi

python3 -m venv word_game 

source word_game/bin/activate

python3 -m ensurepip --upgrade

pip install -r ./requirements.txt

clear

python3 ./main.py