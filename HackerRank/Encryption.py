#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    n = len(s)
    rows = math.floor(math.sqrt(n))
    cols = math.ceil(math.sqrt(n))
    if rows * cols < n:
        rows += 1

    grid = []
    for i in range(0, n, cols):
        grid.append(s[i:i + cols])

    result = []
    for col in range(cols):
        word = ''.join(row[col] for row in grid if col < len(row))
        result.append(word)

    return ' '.join(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
