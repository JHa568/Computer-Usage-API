#!/bin/bash

total=$(top -bn2 | grep 'MiB Mem' | tail -1 | grep -P '(.......|...) total,' | awk '{print $4}')

usage=$(top -bn2 | grep 'MiB Mem' | tail -1 | grep -P '(.......|...) used,' | awk '{print $8}')

mem_usage=$(echo "scale=5; ($usage/$total)*100" | bc)
echo $mem_usage > Pipes/RAM
