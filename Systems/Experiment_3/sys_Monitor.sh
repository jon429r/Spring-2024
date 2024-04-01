#!/bin/bash

# disk function
disk(){
  df -h
}

# mem function
mem(){
  echo "within mem function"
  top -l 1 -n 20
}

# procs [filter] function
procs(){
  echo "within procs function"
  ps aux | grep $2
}

# kill function [pid]
endProcess(){
  kill $1
  read -p "This will end $1 confirm (Y,N)" input
  if [[ $input == "Y" ]]; then
    kill -9 $1
    
    log
    echo "Process $1 killed"
  fi
}

# backup function [source] [destination]
backup(){
  cp $1 $2
  echo "Backup of $1 completed"
}

# find function [directory] [pattern]
find(){
  find $1 -name $2
}

# dupes function [directory]
dupes(){
  echo "Identifying duplicate files in $1 ... This may take a while."
  find $1 -type f -exec md5sum {} \; | sort | uniq -w 32 -dD
  echo 
}

# cleanup function [directory]
cleanup(){
  read -p "This will delete all temp and unnessary files from $1 (Y,N)" confirm
  if [[ $confirm == "Y" ]]; then
    find $1 -type f \( -name "*.tmp -o -name "*.bak" \) -exec rm -f {} \;
    echo "Cleanup completed
  fi
}

# alert threshold function [MEM %]
alertThreshold(){
  memUsed=$(top -l 1 -n 20 | grep PhysMem | awk '{print $2}' | cut -d 'M' -f 1)
  if [[ $1 -gt $memUsed ]]; then
    echo "WARNING: Memory usage exceeds threshold"
  fi
}

# help function
help(){
  echo "Usage: ./sys_Monitor.sh [option] [argument]"
  echo ""
  echo "Options:"
  echo "-disk                Show disk usage for all mounted filesystems, inicating available and used space."
  echo "-mem                 Display a summary of memory usage, including total, used, free, and cached memory."
  echo "-procs [filter]      Show running processes, optionally filtered by a user or commmand name."
  echo "-kill [pid]          Terminate a process by PID."
  echo "-backup [dir] [dest] Create a compressed backup of a specificed directory, with options for destination path."
  echo "-find [directory] [pattern]       Search for files matching a pattern and list their locations."
  echo "-dupes [directory]   Identify duplicate files in a specified directory or the entire filesystem."
  echo "-cleanup [directory] Cleanup specified directory by removing temporary or unnecessary files."
  echo "-alertThreshold [MEM %]           Set alert thresholds for memory usage. If current usage exceeds these thresholds, the script outputs a warning."
  echo "-help                Display this help message and exit."

  exit 0
}

echo "logging"
  if [[ ! -f sys_Monitor.log ]]; then
    touch sys_Monitor.log
  fi
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ($(whoami)) $0 $@" >> sys_Monitor.log


# parse input
while [[ $# -gt 0 ]]; do
  # Execute command based on the first argument $1
  case "$1" in
    -disk)
      disk
      ;;
    -mem)
      mem
      ;;
    -procs)
      procs
      ;;
    -kill)
      # if no PID is provided, exit
      if [[ -z $2 ]]; then
        echo "PID required"
        exit 1
      fi
      endProcess $2
      ;;
    -backup)
      if [[ -z $2 || -z $3 ]]; then
        echo "Source and destination required"
        exit 1
      fi
      backup $2 $3
      ;;
    -find)
      if [[ -z $2 || -z $3 ]]; then
        echo "Directory and pattern required"
        exit 1
      fi
      find $2 $3
      ;;
    -dupes)
      if [[ -z $2 ]]; then
        echo "Directory required"
        exit 1
      fi
      dupes $2
      ;;
    -cleanup)
      if [[ -z $2 ]]; then
        echo "Directory required"
        exit 1
      fi
      cleanup $2
      ;;
    -alertThreshold)
      if [[ -z $2 ]]; then
        echo "Memory threshold required"
        exit 1
      fi
      alertThreshold $2
      ;;
    -help)
      help
      ;;
    *)
      echo "Invalid argument: $1"
      help
      exit 1
      ;;
  esac

  # Shift the arguments to process the next one
  shift
done

