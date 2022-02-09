# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.


# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

def reverse(list):
    middle = round(len(list) / 2)
    for i in range(0, middle, 1):
        temp = list[i]
        list[i] = list [len(list)-1-i]
        list [len(list)-1-i] = temp
    return list

print(reverse(['j','e','n','n','i','f','e','r']))
