# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
# After doing so, return the array.

# Example 1:
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.

def replaceElements(arr):
    i = 0 
    while i < len(arr)-1:
        greatest = arr[i+1]
        for j in range(i+1,len(arr),1):
            if arr[j] > greatest:
                greatest = arr[j]
            arr[i] = greatest
        i+=1

    arr[len(arr)-2] = arr[len(arr)-1]
    arr[len(arr)-1] = -1

    return arr
        

print(replaceElements([57010,40840,69871,14425,70605]))