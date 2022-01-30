#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    alphabet = dict(zip(string.ascii_lowercase, range(0, 26)))
    maxHeight = 0
    for letter in word:
        if h[alphabet.get(letter)] > maxHeight:
            maxHeight = h[alphabet.get(letter)]
    return maxHeight * len(word)

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'output.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
