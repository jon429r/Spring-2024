#!/bin/bash

# A) Validate usernames starting with a letter and consisting of letters, digits, or underscores, 5 to 12 characters in length.
function validate_username() {
    local username="$1"
    local username_regex='^[a-zA-Z][a-zA-Z0-9_]{4,11}$'
    if [[ $username =~ $username_regex ]]; then
        echo "Username: $username - Valid"
    else
        echo "Username: $username - Invalid"
    fi
}

# Test cases for usernames
username_test_cases=(
    "username123"
    "user_name"
    "123username"
    "username_with_underscores"
    "user!name123"
)

# Test each username
for username_case in "${username_test_cases[@]}"; do
    validate_username "$username_case"
done
echo "-----------------------"

# B) Match hexadecimal numbers that start with 0x or 0X.
function match_hexadecimal() {
    local hexadecimal="$1"
    local hexadecimal_regex='^(0x|0X)[0-9a-fA-F]+$'
    if [[ $hexadecimal =~ $hexadecimal_regex ]]; then
        echo "Hexadecimal: $hexadecimal - Valid"
    else
        echo "Hexadecimal: $hexadecimal - Invalid"
    fi
}

# Test cases for hexadecimal numbers
hexadecimal_test_cases=(
    "0x12AB"
    "0XFF"
    "123ABC"
    "0x"
    "0xABCG"
)

# Test each hexadecimal number
for hexadecimal_case in "${hexadecimal_test_cases[@]}"; do
    match_hexadecimal "$hexadecimal_case"
done
echo "-----------------------"

# C) Match passwords that are at least 8 characters long and contain a mix of uppercase and lowercase letters, numbers, and special characters (‘!@#$%^&*()’).
function match_password() {
    local password="$1"
    local password_regex='^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()]).{8,}$'
    if [[ $password =~ $password_regex ]]; then
        echo "Password: $password - Valid"
    else
        echo "Password: $password - Invalid"
    fi
}

# Test cases for passwords
password_test_cases=(
    "password1!"
    "Password123@"
    "securePassword!123"
    "password"
    "12345678"
)

# Test each password
for password_case in "${password_test_cases[@]}"; do
    match_password "$password_case"
done
echo "-----------------------"

# D) Match file names that do not end in specific extensions (e.g., excluding .exe and .tmp files).
function match_file_name() {
    local file_name="$1"
    local file_name_regex='^(?!.*\.exe$)(?!.*\.tmp$).*'
    if [[ $file_name =~ $file_name_regex ]]; then
        echo "File Name: $file_name - Valid"
    else
        echo "File Name: $file_name - Invalid"
    fi
}

# Test cases for file names
file_name_test_cases=(
    "file.txt"
    "document.pdf"
    "application.exe"
    "temporary.tmp"
    "file_without_extension"
)

# Test each file name
for file_name_case in "${file_name_test_cases[@]}"; do
    match_file_name "$file_name_case"
done
echo "-----------------------"
