#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valleys = 0
    total = 0
    
    for step in path:
        initial_negative = total < 0
                
        if step == 'D':
            total += -1
        else:
            total += 1
        
        final_non_negative = total >= 0
        
        if initial_negative and final_non_negative:
            valleys += 1
    
    return valleys
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
