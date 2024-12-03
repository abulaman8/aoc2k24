#!/bin/bash

if [[ $# -ne 1 || ! $1 =~ ^[0-9]+$ ]]; then
  echo "Usage: $0 <numeric argument>"
  exit 1
fi

n=$1

dir_name="day$n"

mkdir -p "$dir_name"

for file in sol1.py sol2.py input.txt test_input.txt; do
  touch "$dir_name/$file"
done

echo "Directory '$dir_name' with files sol1.py, sol2.py, input.txt, and test_input.txt created successfully."
