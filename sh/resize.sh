#!/bin/bash
pkill -f testrender.py
printf '\e[8;32;100t'
python testrender.py
