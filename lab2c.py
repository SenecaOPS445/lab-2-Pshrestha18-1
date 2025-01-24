#!/usr/bin/env python3
# Author: Pranav Shrestha
# Author ID: 113964225
# Date Created: 2025/01/24

import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print("Usage: ./lab2c.py <name> <age>")
    sys.exit(1)

# Extract the command-line arguments
name = sys.argv[1]
age = sys.argv[2]

# Display the result
print(f"Hi {name}, you are {age} years old.")