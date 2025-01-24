#!/usr/bin/env python3

import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print("Usage: ./lab2d.py name age")
    sys.exit(0)  # Exit gracefully if the wrong number of arguments is passed

# Extract the command-line arguments
name = sys.argv[1]
age = sys.argv[2]

# Validate that the age is a positive integer
if not age.isdigit() or int(age) <= 0:
    print("Error: Age must be a positive integer.")
    sys.exit(1)

# Display the result
print(f"Hi {name}, you are {age} years old.")
