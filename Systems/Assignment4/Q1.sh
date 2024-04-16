#!Bin/Bash

echo "Counting status codes of $1"

cat $1 | cut -d' ' -f9 | sort | uniq -c | awk '{print("Status code " $2 ": " $1 " times")}'