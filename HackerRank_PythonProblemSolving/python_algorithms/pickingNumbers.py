#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pickingNumbers function below.
def pickingNumbers(a):
    countNumber = {}
    for i in range(len(a)):
        if a[i] in countNumber:
            countNumber[a[i]] = countNumber[a[i]] + 1
        else:
            countNumber.update({a[i]: 1})

    mostNumber = 0
    maxCount = 0
    for key, value in countNumber:
        if value > maxCount:
            maxCount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a[n])

    fptr.write(str(result) + '\n')

    fptr.close()
