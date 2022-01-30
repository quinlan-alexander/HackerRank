#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if (p-0) > (n-p):
        if n-p == 1 and n%2 == 1:
            return 0
        elif n-p == 1 and n%2 == 0:
            return 1
        else:
            return (n-p)//2
    else:
        return (p-0)//2


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'output.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
