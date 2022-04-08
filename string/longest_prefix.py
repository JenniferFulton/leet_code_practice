# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

def longestCommonPrefix(strs):
    common_prefix = ""
    shortest = len(strs[0])
    arr = []
    
    if len(strs) == 1:
        return(strs[0])
    
    #finding the shortest string in list
    for i in range(len(strs)):
        if len(strs[i]) < shortest:
            shortest = len(strs[i])
            
    # adding all the characters(number of the shortest string) to the array
    for i in range(shortest):
        arr.append(strs[0][i])
    # print(arr)
    
    # comparing values in the array to characters within the strings
    i = 0
    while i <= len(arr)-1:
        for j in range(len(strs)-1):
            if arr[i] == strs[j][j] and arr[i] == strs[j+1][j]:
                common_prefix = common_prefix + arr[i]
            # else:
            #     break
        i += 1

                    
    return common_prefix

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["ab", "a"]))
print(longestCommonPrefix(["reflower","flow","flight"]))