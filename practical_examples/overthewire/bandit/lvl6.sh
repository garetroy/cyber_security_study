#!/bin/sh

password=$(./lvl5.sh)
cmd="find ./inhere/* -type f -size 1033c | xargs grep -L '[^a-zA-Z0-9[:space:]]' | xargs cat"

result=$(python3 login_cached.py 5 $password $cmd)
cleaned_result=$(./cleanup.sh "$result")
echo $cleaned_result
