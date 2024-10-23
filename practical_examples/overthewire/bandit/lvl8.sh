#!/bin/sh

password=$(./lvl7.sh)
cmd="grep -Rw millionth data.txt 2>/dev/null"

result=$(python3 login_cached.py 7 $password $cmd | awk '{print $2}')
cleaned_result=$(./cleanup.sh "$result")
echo $cleaned_result
