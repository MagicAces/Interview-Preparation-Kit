#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positiveCount = 0
    negativeCount = 0
    zeroCount = 0
    
    for digit in arr:
        if digit > 0:
            positiveCount += 1
        elif digit < 0:
            negativeCount += 1
        else:
            zeroCount += 1
            
    print('{x}\n{y}\n{z}'.format(x=float(positiveCount)/len(arr), y=float(negativeCount)/len(arr), z=float(zeroCount)/len(arr)))
         

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
