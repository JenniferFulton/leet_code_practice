# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3

def findMaxConsecutiveOnes(nums):
    cur_max = 0
    new_max = 0
    for i in nums:
        if i == 1:
            new_max += 1
        else:
            if new_max > cur_max:
                cur_max = new_max
            new_max = 0
        if new_max > cur_max:
                cur_max = new_max
    return(cur_max)

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))

# O(N) time complexity