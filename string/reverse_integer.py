# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321



def reverse_int(x):
    if x == 0:
        return 0
    #if it is a negative number
    if x < 0:
        neg_num = str(x * -1)
        list_negNum = list(neg_num)
        
        #reverse the list
        middle = len(list_negNum)//2
        for i in range(middle):
            temp = list_negNum[i]
            list_negNum[i] = list_negNum[len(list_negNum)-1-i]
            list_negNum[len(list_negNum)-1-i] = temp
        
        i = 0
        while i <= len(list_negNum)-1:
            if list_negNum[i]=="0":
                list_negNum.pop(i)
            else:
                break
                
        new_num = ''.join(list_negNum)
        x = int(new_num) * -1
        
        if int(x) < -2**31 or int(x) > 2**31-1:
            return 0
        
        return x
    
    else:
        num = str(x)
        list_num = list(num)
        middle = len(list_num)//2
        for i in range(middle):
            temp = list_num[i]
            list_num[i] = list_num[len(list_num)-1-i]
            list_num[len(list_num)-1-i] = temp
        
        i = 0
        while i <= len(list_num)-1:
            if list_num[0]=="0":
                list_num.pop(i)
            else:
                break
                
        x = ''.join(list_num)
        
    if int(x) < -2**31 or int(x) > 2**31:
        return 0
    
    return x
        
            