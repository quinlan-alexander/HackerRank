#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(a, b):
    aCount = 0
    bCount = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            aCount = aCount + 1
        elif a[i] < b[i]:
            bCount = bCount + 1
    return str(aCount) + str(bCount)

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'output.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = solve(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()