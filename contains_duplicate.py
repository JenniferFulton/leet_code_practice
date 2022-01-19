# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

def contains_duplicate(nums):
    for i in nums:
        if nums.count(nums[i]) > 1:
            return False
        else:
            return True

print(contains_duplicate([1,2,3,4]))
print(contains_duplicate([2,4,4,6]))
