# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]


def threeSum(nums):
    final_arr = []
    for i in range(len(nums)):
        arr = []
        for j in range(i+1,len(nums),1):
            for k in range(j+1,len(nums),1):
                sum = nums[i]+nums[j]+nums[k]
                if sum == 0 and i != j and i != k and j != k:
                    arr.append(nums[i])
                    arr.append(nums[j])
                    arr.append(nums[k])
                    arr.sort()
                    # print(arr)
                    if len(final_arr) == 0:
                        final_arr.append(arr)
                    else:
                        for triplet in final_arr:
                            # print("triplet: ", triplet)
                            if arr == triplet:
                                break
                                
                        final_arr.append(arr)
                    arr = []
                    
    return final_arr

print(threeSum([3,0,-2,-1,1,2]))