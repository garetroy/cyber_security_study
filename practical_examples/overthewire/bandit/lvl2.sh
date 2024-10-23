#!/bin/sh

password=$(./lvl1.sh)

result=$(./login.sh 1 $password 'cat ./-')
cleaned_result=$(./cleanup.sh "$result")
echo $cleaned_result
