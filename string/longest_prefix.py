# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

def longestCommonPrefix(strs):
    common_prefix = ""
    shortest = len(strs[0])
    
    if len(strs) == 1:
        return(strs[0])
    
    #finding the shortest string in list
    for i in range(len(strs)):
        if len(strs[i]) < shortest:
            shortest = len(strs[i])

    return common_prefix

# print(longestCommonPrefix(["flower","flow","flight"]))
# print(longestCommonPrefix(["ab", "a"]))
# print(longestCommonPrefix(["reflower","flow","flight"]))
# print(longestCommonPrefix(["flower","flower","flower","flower"]))
print(longestCommonPrefix(["sunflower"]))