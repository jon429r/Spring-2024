#!/bin/bash

read -p "Enter a number:" num

if [ $num -lt 10 ]; then
  echo "The number is less than 10"
elif [ $num -gt 10 ]; then
  echo "The number is greater than 10"
elif [ $num = 10 ]; then
  echo "The number is 10"
else
  echo "Error: Input is not a number"
fi


