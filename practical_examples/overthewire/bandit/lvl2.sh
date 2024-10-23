#!/bin/sh

password=$(./lvl1.sh)

result=$(python3 login_cached.py 1 $password 'cat ./-')
cleaned_result=$(./cleanup.sh "$result")
echo $cleaned_result
