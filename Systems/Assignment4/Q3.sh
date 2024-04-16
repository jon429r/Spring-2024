#!/usr/bin/env bats

source COS350_A4_Q4.sh

# Test deleteFiles function
@test "Deleting files with matching pattern" {
  curr_dir=$(pwd)
  touch "$curr_dir/file1.tmp"
  touch "$curr_dir/file2.tmp"

  run deleteFiles "$curr_dir" "*.tmp"
  [ "$status" -eq 0 ]
  [ "$output" = "Files matching pattern '*.tmp' have been deleted from $curr_dir" ]
}

# Test appendToFile function
@test "Appending content to file" {
  run appendToFile "source_file.txt" "destination_file.txt"
  [ "$status" -eq 0 ]
  [ "$output" = "Content of source_file.txt has been appended to destination_file.txt" ]
}
