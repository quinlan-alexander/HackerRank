#!/bin/python3

from itertools import cycle
import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
# def minimumSwaps(arr):
#     vis = {x : False for x in range(len(arr))}
#     swaps = 0
#     for i in range(1,len(arr)+1):
#         indexSwap = arr.index(i)
#         if i-1 == indexSwap or vis[i-1]:
#             continue
#         else:
#             # vis[i-1]
#             # arr[i-1], arr[indexSwap] = arr[indexSwap], arr[i-1]
#             swaps += 1
#     return swaps

def minimumSwaps(arr):
    n = len(arr)
    arrpos = [*enumerate(arr)]
    arrpos.sort(key = lambda it : it[1])
    vis = {k : False for k in range(n)}

    ans = 0
    for i in range(n):
        if vis[i] or arrpos[i][0] == i:
            continue

        cycle_size = 0
        j = i

        while not vis[j]:
            vis[j] = True
            j = arrpos[j][0]
            cycle_size += 1
            
        if cycle_size > 0:
            ans += (cycle_size - 1)
        
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
