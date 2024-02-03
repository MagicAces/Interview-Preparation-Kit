#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    freq = 0

    if s.count('a') == 0:
        return 0
        
    if n < len(s):
        return s[:n].count('a')
        
    freq += s.count('a') * int(n / len(s))
    
    if (n % len(s)) != 0:
        freq += s[:(n % len(s))].count('a')
        
    return freq
         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
