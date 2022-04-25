# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.


# Example 1:
# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

def duplicateZeros(arr):
    for i in range (len(arr)-1):
        if arr[i] == 0:
            for j in range(i,len(arr)-1,1):
                arr[j+1] = arr[j]
            arr[i+1] = 0
        

print(duplicateZeros([1,0,2,3,0,4,5,0]))
    