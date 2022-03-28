def remove_dup(nums):
    temp = ""
    for i in nums:
        print("temp is:", temp)
        print("i is:", i)
        if i == temp:
            temp = i
            nums.pop(i)
        else:
            temp = i

    return nums

print(remove_dup([0,0,1,1,1,2,2,3,3,4]))



