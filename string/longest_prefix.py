# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

def longestCommonPrefix(strs):
        common_prefix = ""
        shortest = len(strs[0])
        
        #finding the shortest string in list
        for i in range(len(strs)):
            if len(strs[i]) < shortest:
                shortest = len(strs[i])

        i = 0
        while i <= len(strs):
            for j in range(shortest):
                print(strs[i][j])
                # if strs[i][j] == strs[i+1][j]:
                #     common_prefix = common_prefix + strs[i][j]
            i += 1

longestCommonPrefix(["flower","flow","flight"])