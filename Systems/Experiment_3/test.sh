#!/bin/bash
#
# Test script for sys_Monitor.sh

echo "--------------------"
echo "Testing disk command"
echo "-------------------"
bash sys_Monitor.sh -disk

echo "-------------------"
echo "Testing mem command"
echo "-------------------"
bash sys_Monitor.sh -mem

echo "-------------------------------------"
echo "Testing procs command with parameter"
echo "-------------------------------------"
bash sys_Monitor.sh -procs nvim

echo "----------------------------------------"
echo "Testing procs command without parameter"
echo "----------------------------------------"
bash sys_Monitor.sh -procs

#Create new process to kill

echo "---------------------------"
echo "Testing endProcess command"
echo "----------------------------"
bash sys_Monitor.sh -kill 25324

echo "------------------------"
echo "Testing backup command "
echo "----------------------"

Path=$(pwd)
BackupPath=$(pwd)/backup

bash sys_Monitor.sh -backup "$Path" "$BackupPath"

echo "---------------------"
echo "Testing dupes command"
echo "----------------------"
bash sys_Monitor.sh -dupes $Path

echo "---------------------"
echo "Testing find command"
echo "----------------------"
bash sys_Monitor.sh -find $Path "sys_Monitor.sh"

echo "-------------------------------"
echo "Testing alertThreshold command"
echo "-------------------------------"
bash sys_Monitor.sh -alertThreshold 85

echo "----------------------"
echo "Testing help command"
echo "----------------------"
bash sys_Monitor.sh -help

echo "----------------------"
echo "Printing out log file"
echo "----------------------"
cat sys_Monitor.log | head -n 5
