#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[-2:] == "PM":
        if s[:2] == "12":
            s = s[0:len(s)-2]
            return s
        militaryConvert = int(s[:2]) + 12
        newTime = str(militaryConvert) + s[2:len(s)-2]
        return newTime
    else:
        if s[:2] == "12":
            newTime = '00' + s[2:len(s)-2]
            return newTime
        s = s[0:len(s)-2]
        return s

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'output.txt'
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
