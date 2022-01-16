# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# class Solution:
#     def isPalindrome(self, s: str) -> bool:

def palindrome(s):
    string = str(s.lower())
    new_string = ''
    for value in string:
        if value.isalnum() == True:
            new_string = new_string + value
    if new_string == new_string[::-1]:
        return True
    else:
        return False

print(palindrome("Hi! My name is Jennifer"))
print(palindrome("racecar"))
