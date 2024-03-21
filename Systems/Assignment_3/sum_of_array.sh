#!/bin/bash

# declare array [1...10] 

myArray=(1 2 3 4 5 6 7 8 9 10)

# loop to calculate the sum
sum=0

for num in ${myArray[@]}; do
  let sum+=$num
done

echo $sum
