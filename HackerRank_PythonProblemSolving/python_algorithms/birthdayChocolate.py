#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s, d, m):
    countOfWays = 0
    for i in range(len(s)-m+1):
        sum = 0
        for j in range(i, i+m):
            sum = sum + s[j]
        if sum == d:
            countOfWays = countOfWays + 1
    return countOfWays


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'output.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = list(map(int, input().rstrip().split()))

    dm = input().split()

    d = int(dm[0])

    m = int(dm[1])

    result = solve(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
