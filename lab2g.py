#!/usr/bin/env python3
# Author: Pranav Shrestha
# Author ID: 113964225
# Date Created: 2025/01/24

# Importing required module
import sys

# Default timer value
if len(sys.argv) < 2:
    timer = 3
else:
    try:
        timer = int(sys.argv[1])
    except ValueError:
        print("Error: Please provide a valid number.")
        sys.exit(1)

# Countdown loop
while timer > 0:
    print(timer)
    timer -= 1

# Print final message
print("blast off!")