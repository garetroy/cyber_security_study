#!/bin/sh

password=$(./lvl4.sh)
cmd="grep -L '[^a-zA-Z0-9[:space:]]' ./inhere/* | xargs cat"


result=$(python3 login_cached.py 4 $password $cmd)
cleaned_result=$(./cleanup.sh "$result")
echo $cleaned_result
