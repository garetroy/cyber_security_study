#!/bin/sh

password=$(./lvl10.sh)
cmd='base64 -d data.txt'

result=$(python3 login_cached.py 10 $password $cmd | awk '{print $4}')
cleaned_result=$(./cleanup.sh "$result")
echo $cleaned_result
