#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    diagonalOne = 0
    diagonalTwo = 0
    indexD1 = 0
    indexD2 = len(arr) - 1
    for i in arr:
        diagonalOne = diagonalOne + i[indexD1]
        diagonalTwo = diagonalTwo + i[indexD2]
        indexD1 = indexD1 + 1
        indexD2 = indexD2 - 1
    return(abs(diagonalOne-diagonalTwo))

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'output.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()