#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sums = set()
    for i in range(len(arr)):
        sums.add(sum(arr) - arr[i])
    print(str(min(sums)) + " " + str(max(sums)))

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5];

    miniMaxSum(arr)