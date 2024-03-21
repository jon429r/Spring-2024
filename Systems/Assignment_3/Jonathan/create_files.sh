#!/bin/bash

# Create 100 files named text1.txt ... text100.txt

for ((i=1; i<=100; i++)); do
  touch test${i}.txt
done
