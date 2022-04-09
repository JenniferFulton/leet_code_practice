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
    # while loop with go the length of arr to account for every character
    while i <= len(arr)-1:
        #for loop will account for every word
        for j in range(len(strs)-1):
            # if the character in the arr doesn't equal the character in the string(strs[i])
            # and the string after it return common prefix
            current_char = arr[i]
            current_string = strs[j]
            if arr[i] == strs[j][i]:
                common_prefix = common_prefix + arr[i]
            else:
                # if they are all equal, add it to the common prefix
                return(common_prefix)
                
            i += 1

                    
    return common_prefix

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["ab", "a"]))
print(longestCommonPrefix(["reflower","flow","flight"]))
print(longestCommonPrefix(["flower","flower","flower","flower"]))