#!/bin/bash

##Count the number of files in the current directory

echo "The number of files is:" $(ls -l | grep ^- | wc -l)
