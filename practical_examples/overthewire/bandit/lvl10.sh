#!/bin/sh

password=$(./lvl9.sh)
cmd='grep -ao "=\ [a-zA-Z0-9]\+" data.txt | tail -n 1 | tr -d "="'

result=$(python3 login_cached.py 9 $password $cmd)
cleaned_result=$(./cleanup.sh "$result")
echo $cleaned_result
