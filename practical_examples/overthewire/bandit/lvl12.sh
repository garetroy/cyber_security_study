#!/bin/sh

password=$(./lvl11.sh)
cmd="cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'"

result=$(python3 login_cached.py 11 $password $cmd | awk '{print $4}')
cleaned_result=$(./cleanup.sh "$result")
echo $cleaned_result
