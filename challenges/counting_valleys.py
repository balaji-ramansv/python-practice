#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    current = 0
    navigating_mounain = False
    navigating_valley = False
    valley_count = 0
    mountain_count = 0
    for i, step in enumerate(path):
        prev = None
        if i > 0:
            prev = path[i-1]
        if step == "U":
            current += 1
        elif step == "D":
            current -= 1
        if current >= 2:
            navigating_mounain = True
        elif current <= -2:
            navigating_valley = True
        if navigating_mounain and (current == 0 or prev == "D"):
            mountain_count += 1
            navigating_mounain = False
        elif navigating_valley and (current == 0 or (prev == "U")):
            valley_count += 1
            navigating_valley = False
    return valley_count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #steps = int(input().strip())

    #path = input()

    #result = countingValleys(steps, path)
    result = countingValleys(10, "DUDDDUUDUU")
    

    #fptr.write(str(result) + '\n')

    #fptr.close()

    print(result)
