# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# class Solution:
#     def isPalindrome(self, s: str) -> bool:

def palindrome(s):
    string = str(s.lower())
    for value in string:
        if value.isalnum() == True:
            print(value)
    #     else:
    #         string.replace(value,'')
    # print (string)
    # return (string)

print(palindrome("Hi! My name is Jennifer"))
