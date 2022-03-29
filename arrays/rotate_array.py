# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]


def rotate(nums,k) -> None:
    if k > len(nums)-1:
        print("Please provide number that is shorter than the length of the list!")
    else:
        new_array = []
        runner = k + 1
        while runner <= len(nums)-1:
            new_array.append(nums[runner])
            runner += 1
            # print("runner is:", runner)
        
        i=0
        while i <= k:
            # print("i is:", i)
            new_array.append(nums[i])
            i += 1
        
        print(new_array)
        return(new_array)

print(rotate([1,2,3,4,5,6,7],8))