#!/usr/bin/env python3
import sys

# Ensure that a command-line argument was provided
if len(sys.argv) != 2:
    sys.exit(1)  # Exit with an error if no argument is provided

# Get the countdown number from the argument
try:
    count = int(sys.argv[1])
except ValueError:
    sys.exit(1)  # Exit with an error if the argument is not a valid integer

# Countdown from the given number
while count > 0:
    print(count)
    count -= 1

# After countdown, print "blast off!"
print("blast off!")
