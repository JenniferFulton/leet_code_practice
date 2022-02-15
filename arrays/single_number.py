# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1


def single_num(nums):
    single = nums[0]
    for i in nums:
        if nums[i] == single:
            pass
        else:
            nums[i]=single
    return (single)

print(single_num([2,2,1]))
