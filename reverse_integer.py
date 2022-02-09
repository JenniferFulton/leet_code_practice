# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

def reverse_int(x):
    num = str(x)
    for i in range(round(len(num)/2)):
        temp = num[i]
        num[i] = num[len(num)-1-i]
        num[len(num)-1-i] = temp

    return(int(num))

print(reverse_int(6509))