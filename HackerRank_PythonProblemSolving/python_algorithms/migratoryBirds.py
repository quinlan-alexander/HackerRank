#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(ar):
    countBirds = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0}

    for i in range(len(ar)):
        countBirds[str(ar[i])] = countBirds[str(ar[i])] + 1

    maxValue = max(countBirds.values())
    maxIDs = list()

    for key, value in countBirds.items():
        if value == maxValue:
            maxIDs.append(key)

    return min(maxIDs)


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'output.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = migratoryBirds(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
