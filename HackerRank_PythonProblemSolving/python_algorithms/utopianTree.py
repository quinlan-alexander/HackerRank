#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        height = 2 ** ((n/2) + 1) - 1
        return int(height)
    elif n % 2 == 1:
        height = 2 ** ((n+3)/2) - 2
        return int(height)

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'output.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
