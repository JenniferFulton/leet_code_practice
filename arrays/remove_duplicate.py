# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique 
# element appears only once. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, 
# you must instead have the result be placed in the first part of the array nums. 
# More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
# It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# EX 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

def remove_duplicate(nums):
#     i = 0
#     while i <= len(nums)-2:
#         if nums[i] == nums[i+1]:
#             nums.pop(i+1)
#         else:
#             i += 1
#     return (nums)

# print(remove_duplicate([-1,0,0,0,0,3,3]))

# solve without pop
    if len(nums) == 1:
        return 1
    else:
        i = 0
        k = len(nums)-1
        while i < k:
            if nums[i] == nums[i+1]:
                for j in range(i+1, len(nums),1):
                    nums[j-1] = nums[j]
                k -= 1
            else:
                i += 1
        return k+1

print(remove_duplicate([1,1,2,3,3,4,5,5,5]))