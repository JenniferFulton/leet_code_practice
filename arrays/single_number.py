# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1


def single_num(nums):
    for i in nums:
        if nums.count(i) == 1:
            return i

# print(single_num([2,2,1]))
print(single_num([4,1,2,1,2]))
