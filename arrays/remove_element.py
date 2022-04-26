def removeElement(nums, val):
    i = 0
    length = len(nums)
    while i < length:
        if nums[i] == val:
            for j in range(i+1, len(nums),1):
                nums[j-1] = nums[j]
            length -= 1
            i = 0
        else:
            i += 1
        # else:
        #     i += 1
    return nums

print(removeElement([0,1,2,2,3,0,4,2],2))


