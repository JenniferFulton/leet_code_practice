# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

def plus_one(digits):
    # set current index to last place in digits
    index = len(digits) - 1

    # increment "9" places that cause spill over
    while (index >= 0 and digits[index] == 9):
        # if it is 9, set it to 0 and move the index to the next highest digit
        digits[index] = 0
        index -= 1

    if index >= 0:
        # increment current place by 1
        digits[index] =  digits[index] + 1
    else:
        # if index is 0 it means there was a "9 spillover" in highest digit and need to add a 1 to the front
        digits.insert(0, 1)

    return digits


    # digit_string = ""
    # array = []

    # for i in digits:
    #     digit_string = digit_string + str(i)

    # integer = int(digit_string) + 1

    # for i in str(integer):
    #     array.append(i)
    
    # return array

# while 
    
    # if digits[len(digits)-1] == 9:
    #     digits.append(0)
    #     digits[len(digits)-2] += 1

        
    # else:
    #     digits[len(digits)-1] += 1
    
    # return digits

print(plus_one([1,9,4]))
# print(plus_one([9, 9]))

#O(n)^2 because it has to iterate twice
# or is it o(n) since it iterates 2 different objects once