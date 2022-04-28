# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

# Example 1:
# Input: arr = [3,5,5]
# Output: false

# Example 2:
# Input: arr = [0,3,2,1]
# Output: true

def validMountainArray(arr):
    if len(arr) < 3:
        return False

    # find the peak
    peak = arr[0]
    for i in arr:
        if i > peak:
            peak = i
    print("peak is:", peak)

    # make sure peak is not on the end of the mt
    if peak == arr[0] or peak == arr[len(arr)-1]:
        return False
    
    # Need to find the index of the peak
    peak_index = 0
    for i in range(len(arr)):
        if arr[i] == peak:
            peak_index = i
    print("peak index:", peak_index)

    # up the mt
    for i in range(peak_index):
        print("up:",arr[i])
        if arr[i] >= arr[i+1]:
            return False
    # down the mt
    for i in range(peak_index, len(arr)-1, 1):
        print("down:",arr[i])
        if arr[i] <= arr[i+1]:
            return False

    return True
        

print(validMountainArray([0,1,2,4,2,1]))
print(validMountainArray([0,1,3,4,1]))
print(validMountainArray([3,5,5]))