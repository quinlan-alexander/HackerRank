#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    for i in range(len(grades)):
        roundUp = ((grades[i] // 5) + 1) * 5
        if grades[i] < 38:
            continue
        elif roundUp - grades[i] < 3:
                grades[i] = roundUp
    return grades

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'output.txt'
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
