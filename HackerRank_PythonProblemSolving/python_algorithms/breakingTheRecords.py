#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    breakRecordsCount = list()
    countHigh = 0
    countLow = 0
    max = scores[0]
    min = scores[0]
    for i in range(len(scores)):
        if scores[i] > max:
            max = scores[i]
            countHigh = countHigh + 1
        if scores[i] < min:
            min = scores[i]
            countLow = countLow + 1
    breakRecordsCount.append(countHigh)
    breakRecordsCount.append(countLow)
    return breakRecordsCount

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'output.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
