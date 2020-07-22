#!/bin/bash
set -euo pipefail
IFS=$'\n\t'


RESULT=$(python3 elves.py elves_masses_test_2020.txt)
echo $RESULT
if [  $RESULT == "8" ] 
  then 
  exit 1
fi