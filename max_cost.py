#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. STRING_ARRAY labels
#  3. INTEGER dailyCount
#

def maxCost(cost, labels, dailyCount):
    cost_label = zip(cost, labels)
    day_cost = []
    dc = 0
    current_cost = 0
    for cl in cost_label:
        price, label = cl
        day_cost.append(0)
        if label == 'legal' and dc != dailyCount:
            dc += 1
            day_cost[-1] += price
            if label == 'legal' and dc == dailyCount:
                #day_cost.append(current_cost)
                dc = 0
                #current_cost = 0
        elif label == 'illegal' and dc != dailyCount:
            current_cost += price
    
    return max(day_cost)


if __name__ == '__main__':
    print(maxCost([1], ['illegal'], 1))
