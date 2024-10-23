#!/bin/sh

cleaned_result=$(echo "$1" | tr -d '\r' | tr -d '\n')
echo $cleaned_result
