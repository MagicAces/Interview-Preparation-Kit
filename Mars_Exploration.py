#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    mutated_count = 0
    
    for i in range(len(s) // 3):
        if s[i*3] != 'S':
            mutated_count += 1
        if s[i*3 + 1] != 'O':
            mutated_count += 1
        if s[i*3 + 2] != 'S':
            mutated_count += 1
    
    return mutated_count 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
