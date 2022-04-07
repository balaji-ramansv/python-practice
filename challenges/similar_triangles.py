#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'nearlySimilarRectangles' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts 2D_LONG_INTEGER_ARRAY sides as parameter.
#

def nearlySimilarRectangles(sides):
    similar = 0
    for ix, side in enumerate(sides):
        if ix + 1 <= len(sides) - 1:
            rest = sides[ix+1:]
            for another_side in rest:
                if side[0]/another_side[0] == side[1]/another_side[1]:
                    similar += 1
    return similar

if __name__ == '__main__':
    result = nearlySimilarRectangles([[5,10], [10,10], [3,6], [9,9]])
    print(result)
