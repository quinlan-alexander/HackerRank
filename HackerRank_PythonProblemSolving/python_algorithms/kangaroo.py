#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if x1 < x2:
        if v1 <= v2:
            return "NO"
        elif v1 > v2:
            jumps = (x2-x1)/(v1-v2)
            if jumps.is_integer():
                return "YES"
            else:
                return "NO"
    elif x2 < x1:
        if v2 <= v1:
            return "NO"
        elif v2 > v1:
            jumps = (x2-1)/(v1-v2)
            if jumps.is_integer():
                return "YES"
            else:
                return "NO"



if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'output.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
