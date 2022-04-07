#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def array_manipulation(n, queries):
    arr_list = [ 0 for i in range(n)]
    long_list = []
    for q in queries:
        for j in range(q[0] - 1, q[1]):
            arr_list[j] += q[2]
    return max(arr_list)

if __name__ == '__main__':
    n = 5
    m = 3
    queries = [[1,2,100], [2,5,100], [3,4,100]]
    result = array_manipulation(n, queries)
    print(result)

