# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321



def reverse_int(x):
    # num = str(x)
    # return(int(num[::-1]))

    if x < 0:
        neg_num = str(x * -1)
        length = len(neg_num)
        middle = round(length/2)
        for i in range(middle):
            neg_num.replace(neg_num[i],neg_num[length-1-i]) 
            neg_num.replace(neg_num[length-1-i],num[i])
        return(int(neg_num * -1))
    else:
        num = str(x)
        length = len(num)
        middle = round(length/2)
        for i in range(middle):
            temp = num[i]
            num = num.replace(num[i],num[length-1-i]) 
            num = num.replace(num[length-1-i],temp)
        return(int(num))
    
print(reverse_int(1234))

string = "Jennifer"
print(string.replace("f","B",1))