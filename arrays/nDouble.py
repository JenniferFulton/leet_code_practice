# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
# More formally check if there exists two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

# Example 1:
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

def checkIfExist(arr):
    i = 0
    if arr.count(0) > 1:
        return True
    else:
        while i < len(arr):
            n = arr[i]
            for j in range(len(arr)):
                m = arr[j]
                if n != m and n == m * 2:
                    return True
            i += 1
    return False

print(checkIfExist([-2,0,10,-19,4,6,-8]))

