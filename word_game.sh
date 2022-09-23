#!/bin/bash

clear

if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, check out https://installpython3.com/' >&2
  exit 1
fi

python3 -m venv word_game 

cd word_game

source bin/activate

python3 install pip

pip install -r ../src/requirements.txt

cp ../src/dic.txt .

python3 ../src/main.py