#!/bin/sh

cmd='cat spaces*'
password=$(./lvl2.sh)

result=$(python3 login_cached.py 2 $password $cmd)
cleaned_result=$(./cleanup.sh "$result")
echo $cleaned_result
