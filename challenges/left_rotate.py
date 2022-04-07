#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def rotate_left(d, arr):
    rem = arr[0:d]
    for i in range(d):
        del arr[0]
    arr.extend(rem)
    return arr

if __name__ == '__main__':
    result = rotate_left(4, [1,2,3,4,5])
    print(result)
