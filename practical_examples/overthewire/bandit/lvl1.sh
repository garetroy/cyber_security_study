#!/bin/sh

result=$(python3 login_cached.py 0 bandit0 "grep 'password' readme")

cleaned_result=$(./cleanup.sh "$result")

password=$(echo "$cleaned_result" | awk '{print $NF}')
echo $password

