# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

from tkinter import Place


def sortedSquares(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2
    nums.sort()
    return (nums)

# O(1) space compexity
#     modified in Place
# sort method makes time compxity O(logN)