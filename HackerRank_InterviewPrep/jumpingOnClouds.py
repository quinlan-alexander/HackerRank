#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    currentCloud = 0
    steps = 0
    
    while (currentCloud != len(c)-1):
        if (currentCloud + 2) < len(c) and c[currentCloud+2] == 0:
            currentCloud += 2
            steps += 1
        elif c[currentCloud+1] == 0:
            currentCloud += 1
            steps += 1
        print(currentCloud)
    return steps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
