#!/bin/sh

password=$(./lvl6.sh)
cmd="find /* -type f -size 33c -user bandit7 -group bandit6 2>/dev/null | xargs cat"

result=$(python3 login_cached.py 6 $password $cmd)
cleaned_result=$(./cleanup.sh "$result")
echo $cleaned_result
