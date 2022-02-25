# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        front_index = 0
        back_index = len(s) - 1
        
        while front_index < back_index:
            # print('iterate')
            
            if s[front_index].isalnum() == False:
                # print(f"skip front {front_index}, '{s[front_index].lower()}'")
                front_index += 1
                continue
            
            if s[back_index].isalnum() == False:
                # print(f"skip back {back_index}, {s[back_index].lower()}")
                back_index -= 1
                continue
            
            # print(f"[{front_index}, {back_index}] {s[front_index].lower()} == {s[back_index].lower()}")
            
            if s[front_index].lower() != s[back_index].lower():
                return False
            else:
                front_index += 1
                back_index -= 1
            
        return True
    
