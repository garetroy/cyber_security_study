#!/bin/sh

password=$(./lvl13.sh)

cmd="cat sshkey.private"

result=$(python3 login_cached.py 13 $password $cmd)

fixed_result=$(echo "$result" | fold -w 64)

printf "%s\n" "$fixed_result"
