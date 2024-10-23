#!/bin/sh

password=$(./lvl3.sh)

result=$(python3 login_cached.py 3 $password 'cat inhere/.*')
cleaned_result=$(./cleanup.sh "$result")
echo $cleaned_result
