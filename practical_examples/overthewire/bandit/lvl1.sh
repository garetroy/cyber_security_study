#!/bin/sh

result=$(./login.sh 0 bandit0 "grep 'password' readme")

cleaned_result=$(./cleanup.sh "$result")

password=$(echo "$cleaned_result" | awk '{print $NF}')
echo $password

