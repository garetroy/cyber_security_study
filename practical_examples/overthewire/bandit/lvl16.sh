#!/bin/sh

password=$(./lvl15.sh)

cmd="echo \"$password\" | ncat --ssl localhost 30001"

result=$(python3 login_cached.py 15 $password $cmd)

cleaned_result=$(./cleanup.sh "${result#*Correct!}")
echo $cleaned_result
