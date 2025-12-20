#!/bin/bash
cat 8.txt | tr -d '\n' | split -b 32 --filter 'dd 2> /dev/null; echo' | sort | uniq -c | sort -n | grep -v '^[ ]*1 '|awk '{print $2}'
