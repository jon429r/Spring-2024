#!/bin/bash

# Deletes files matching a pattern within a directory.
# Usage: deleteFiles <directory_path> <pattern>
deleteFiles() {
  local dir_path=$1
  local pattern=$2

  # Check if the directory exists
  if [ ! -d "$dir_path" ]; then
    echo "Directory does not exist: $dir_path"
    return 1
  fi

  # Navigate to the directory
  cd $dir_path 

  # Find and delete files matching the pattern
  find . -type f -name $pattern -exec rm -f {} \;
  echo "Files matching pattern '$pattern' have been deleted from $dir_path"
}

# Appends the content of one file to another.
# Usage: appendToFile <source_file> <destination_file>
appendToFile() {
  local src_file=$1
  local dest_file=$2

  # Check if the source file exists
  if [ ! -f "$src_file" ]; then
    echo "Source file does not exist: $src_file"
    return 1
  fi

  # Append the content
  cat $src_file >> "$dest_file"
  echo "Content of $src_file has been appended to $dest_file"
}
