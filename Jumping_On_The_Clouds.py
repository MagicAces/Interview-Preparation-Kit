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
    # Write your code here
    jumps = 0
    plus = 0
    prev = c[0]
    
    for i in range(1, len(c)):
        
        if c[i] == 0:
            if plus > 0:
                jumps += 1
                plus = 0
            else:
                if i + 1 < len(c) and prev == 0 and c[i + 1] == 0:
                    plus += 1
                else:
                    jumps += 1
        
        prev = c[i]
        
    return jumps
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
