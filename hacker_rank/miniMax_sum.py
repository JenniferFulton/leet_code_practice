# Given five positive integers, find the minimum and maximum values that can be calculated by 
# summing exactly four of the five integers. Then print the respective minimum and 
# maximum values as a single line of two space-separated long integers.

# Example 
# [1,3,5,7,9]
# The minimum sum is 1+3+5+7 and the maximum sum is 3+5+7+9. The function prints
# 16 24

#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    min_sum = arr[0] + arr[1] + arr[2] + arr[3]
    max_sum = arr[len(arr)-1] + arr[len(arr)-2] + arr[len(arr)-3] + arr[len(arr)-4]
    print(min_sum,  max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
