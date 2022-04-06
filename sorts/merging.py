def merge(nums1,m,nums2,n):    
    # if m=0 no values from nums1 will carry over to the new array, remove them all
    if m == 0:
        nums1 = []
            
    # remove the part of nums1 that will not be included in the final array        
    else:
        i = len(nums1)-1
        while i >= m:
            nums1.pop(i)
            i -= 1
    
    if n == 0:
        return (nums1.sort())
    else:
        for i in range(n):
            nums1.append(nums2[i])
            
    if len(nums1) == 1:
        return nums1
    else:
        return(nums1.sort())

print(merge([0],0,[1],1))
            