#!/bin/sh

password=$(./lvl8.sh)
cmd="sort data.txt | uniq -u"

result=$(python3 login_cached.py 8 $password $cmd)
cleaned_result=$(./cleanup.sh "$result")
echo $cleaned_result
