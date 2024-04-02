#!/bin/bash

# disk function
disk(){
  echo "Disk usage for all mounted filesystems:"
  echo "---------------------------------------"
  df -h | awk '{print $5 " Percent used on " $1 }'
  exit 0
}

mem() {
  echo "Memory usage summary:"
  echo "----------------------"

  totalMem=$(( $(sysctl -n hw.memsize) / 1024 / 1024 ))

  echo "Total Memory: $totalMem MB"

  top -l 1 -n 20 | grep PhysMem | awk -v total="$totalMem" '{print "Total Memory Used: " $2 ", Free Memory: " total - $2 " MB"}'
  exit 0
}

# procs [filter] function
procs(){
  echo "Showing all running processes"
  if [[ -z $1 ]]; then
    ps aux
  else
    # show UID PID PPID TTY STIME COMMAND
    ps aux | grep $1 | awk '{print $1, $2, $3, $4, $5, $11}'
  fi
  exit 0
}

endProcess(){
  pid=$1
  if ps -p $pid > /dev/null; then
    read -p "This will end $pid. Confirm (Y/N): " input
    if [[ $input == "Y" || $input == "y" ]]; then
      kill -9 "$pid"
      echo "Process $pid killed."
    else
      echo "Operation cancelled."
      exit 1
    fi
  else
    echo "Process with PID $pid is not running."
  fi
  exit 0
}

# backup function [source] [destination]
backup(){
  echo "Creating backup of $1 in $2 ..."
  tar -czf $2/backup_$(date '+%Y-%m-%d_%H-%M-%S').tar.gz $1
  if [ $? -eq 0 ]; then
    echo "Backup created successfully."
  else
    echo "Backup failed."
    exit 1
  fi
  exit 0
}

dupes() {
  echo "Finding duplicate files in $1"
  dir=$1
  
  # Use null termination and process substitution to handle filenames with spaces
  while IFS= read -r -d '' file; do
    md5=$(md5sum "$file" | cut -d' ' -f1)
    printf "%s %s\n" "$md5" "$file"
  done < <(find "$dir" -maxdepth 1 -type f -print0)

  # Check if duplicate search command succeeded
  if [ ${PIPESTATUS[0]} -eq 0 ]; then
    echo "Search completed."
  else
    echo "Search failed."
    exit 1
  fi
}

# find function [directory] [pattern]
find(){
  echo "Searching $1 for files matching pattern $2 ..."
  ls -R "$dir" | grep -- "$pattern"
  if [ $? -eq 0 ]; then
    echo "Search completed."
  else
    echo "Search failed."
    exit 1
  fi
  exit 0
}

# cleanup function [directory]
cleanup(){
  echo "Cleaning up $1"
  rm -rf "$1"/*.tmp
  rm -rf "$1"/*.bak
  if [ $? -eq 0 ]; then
    echo "Cleanup completed."
  else
    echo "Cleanup failed."
    exit 1
  fi
  exit 0

}
alertThreshold() {
  # Retrieve total memory size
  threshold=$1
  while true; do
    totalMem=$(( $(sysctl -n hw.memsize) / 1024 / 1024 ))
    memory_info=$(top -l 1 -n 20 | awk '/PhysMem/ {print $2, $4}' | sed 's/M//g')
    memUsed=$(echo "$memory_info" | awk '{print $1}')
    percentageUsed=$(echo "scale=0; $((memUsed * 100)) / $totalMem" | bc)

    echo "Checking memory usage..."
    echo "Memory Usage: $percentageUsed%"
    echo "Threshold: $threshold%"
    # Check if memory information retrieval failed
    if [ -z "$totalMem" ] || [ -z "$memUsed" ]; then
      echo "Failed to retrieve memory information. Check if top command output format has changed."
      exit 1
    fi

    # Check if the threshold value is valid
    if [ "$1" -gt 100 ] || [ "$1" -lt 0 ]; then
      echo "Invalid threshold value. Please enter a value between 0 and 100."
      exit 1
    fi
    # Check if memory usage exceeds the threshold
    if [ "$percentageUsed" -gt "$threshold" ]; then
      echo "WARNING: Memory usage $percentageUsed% exceeds $1% threshold"
      exit 1
    fi
    sleep 5
  done
  exit 0
}

# Example usage: alertThreshold 90
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
      shift
      ;;
    -mem)
      mem
      shift
      ;;
    -procs)
      procs
      shift
      ;;
    -kill)
      # if no PID is provided, exit
      if [[ -z $2 ]]; then
        echo "PID required"
        exit 1
      fi
      endProcess $2
      shift 2
      ;;
    -backup)
      if [[ -z $2 || -z $3 ]]; then
        echo "Source and destination required"
        exit 1
      fi
      backup $2 $3
      shift 2
      ;;
    -find)
      if [[ -z $2 || -z $3 ]]; then
        echo "Directory and pattern required"
        exit 1
      fi
      find $2 $3
      shift 2
      ;;
    -dupes)
      if [[ -z $2 ]]; then
        echo "Directory required"
        exit 1
      fi
      dupes $2
      shift 2
      ;;
    -cleanup)
      if [[ -z $2 ]]; then
        echo "Directory required"
        exit 1
      fi
      cleanup $2
      shift 2
      ;;
    -alertThreshold)
      if [[ -z $2 ]]; then
        echo "Memory threshold required"
        exit 1
      fi
      alertThreshold $2
      shift 2
      ;;
    -help)
      help
      shift
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

