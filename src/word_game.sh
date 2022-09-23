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

source word_game/bin/activate

pwd

python3 install pip

pip install -r ./requirements.txt

cp ./dic.txt .

clear

python3 ./main.py