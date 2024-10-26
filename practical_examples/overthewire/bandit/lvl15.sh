#!/bin/sh

password=$(./lvl14.sh)

cmd="cat /etc/bandit_pass/bandit14 | nc localhost 30000"

result=$(python3 login_cached.py 14 "$password" $cmd)

cleaned_result=$(./cleanup.sh "${result#*Correct!}")
echo $cleaned_result
