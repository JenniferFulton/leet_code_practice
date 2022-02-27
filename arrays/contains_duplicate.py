# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

def contains_duplicate(nums):
    have_seen = {}
    for i in nums:
        # check if i is in dictionay
        if have_seen.get(i) == None:
            #if not add it to the dictionary and keep going
            have_seen[i] = True
            #if it is already in the dictionary return True
        else:
            return True
    return False


print(contains_duplicate([2,14,18,22,22]))
print(contains_duplicate([2,4,4,6]))
print(contains_duplicate([1,2,3,4]))


