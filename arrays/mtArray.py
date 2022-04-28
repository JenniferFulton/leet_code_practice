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
    middle =  len(arr)//2    
    
    # going up the mt
    i = 0
    while i < middle:
        print("up:", arr[i])
        if arr[i] <= arr[i+1]:
            i += 1
        else:
            return False

    # going down mt
    j = len(arr)-1
    while j > middle:
        print("down:", arr[j])
        if arr[j] <= arr[j-1]:
            j -= 1
        else:
            return False
        
    return True
        

print(validMountainArray([0,1,2,4,2,1]))
print(validMountainArray([0,3,2,1]))
print(validMountainArray([3,5,5]))