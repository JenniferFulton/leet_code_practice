# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
# Print the decimal value of each fraction on a new line with  places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, 
# though answers with absolute error of up to  are acceptable.

# Example 
# arr = [1,1,0,-1,-1]
# There are n=5 elements, two positive, two negative and one zero. Results are printed as:
# 0.400000
# 0.400000
# 0.200000

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
    pos_count = 0
    neg_count = 0
    zero_count = 0
    for i in arr: 
        if i > 0:
            pos_count += 1
            # print("positivie numbers:", pos_count)
        if i < 0:
            neg_count += 1
            # print("negative numbers:", neg_count)
        if i == 0:
            zero_count += 1
            # print("zeros:", zero_count)
    print("{:.6f}".format(pos_count/n))
    print("{:.6f}".format(neg_count/n))
    print("{:.6f}".format(zero_count/n))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

# This would be an O(n) solution because we have to look at each value in arr. Making 3 new values is costly
# when thinking about space complexity but it won't get better than O(n) run time. 
