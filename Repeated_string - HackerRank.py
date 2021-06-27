#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    initialCount = 0

    for i in range(len(s)):
        if s[i] == 'a':
            initialCount += 1

    strCount = n // len(s)
    aCount = strCount * initialCount
    charLeft = strCount * len(s)

    i = 0
    while charLeft < n:
        if s[i] == 'a':
            aCount += 1
        charLeft += 1
        i += 1
    
    return aCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
