#!/bin/bash

# Deletes files matching a pattern within a directory.
# Usage: deleteFiles <directory_path> <pattern>
deleteFiles() {
  local dir_path="$1"
  local pattern="$2"

  # Check if the directory exists
  if [ ! -d "$dir_path" ]; then
    echo "Error: Directory does not exist: $dir_path"
    return 1
  fi

  # Navigate to the directory
  if ! cd "$dir_path"; then
    echo "Error: Failed to change directory to $dir_path"
    return 1
  fi

  # Find and delete files matching the pattern
  if ! find . -type f -name "$pattern" -exec rm -f {} \;; then
    echo "Warning: No files matching pattern '$pattern' found in $dir_path"
  else
    echo "Files matching pattern '$pattern' have been deleted from $dir_path"
    return 0
  fi
}

# Appends the content of one file to another.
# Usage: appendToFile <source_file> <destination_file>
appendToFile() {
  local src_file="$1"
  local dest_file="$2"

  # Check if the source file exists
  if [ ! -f "$src_file" ]; then
    echo "Error: Source file does not exist: $src_file"
    return 1
  fi

  # Append the content
  if ! cat "$src_file" >> "$dest_file"; then
    echo "Error: Failed to append content from $src_file to $dest_file"
    return 1
  fi

  echo "Content of $src_file has been appended to $dest_file"
  return 0
}
