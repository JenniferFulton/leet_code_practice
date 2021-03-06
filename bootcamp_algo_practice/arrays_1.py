# 1. Shuffle
# In JavaScript, the Array object has numerous useful methods. 
# It does not, however, contain a method that will randomize the order of an array’s elements. 
# Let’s create shuffle(arr), to efficiently shuffle a given array’s values. Work in-place, naturally. 
# Do you need to return anything from your function?
import random
def shuffle(array):
    random.shuffle(array)
    return array

print(shuffle([5,7,8,1,3,65]))

# 2. Skyline Heights
# Lovely Burbank has a breathtaking view of the Los Angeles skyline. 
# Let’s say you are given an array with heights of consecutive buildings, starting closest to you and extending away. 
# Array [-1,7,3] would represent three buildings: first is actually out of view below street level, 
# behind it is second at 7 stories high, third is 3 stories high (hidden behind the 7-story). 
# You are situated at street level. Return array containing heights of buildings you can see, in order. 
# Given [-1,1,1,7,3] return [1,7]. Given [0,4] return [4]. As always with challenges, do not use built-in array functions such as unshift().

def skyline(array):
    visible = []
    for i in range(len(array)-1):
        if array[i] <= 0:
            pass
        if array[i] <= array[i-1]:
            pass
        else:
            visible.append(array[i])
    print(visible)

skyline([-1,1,1,7,3])


# 3. Zip It
# Create a standalone function that accepts two arrays and combines their values sequentially into a new array. 
# Extra values from either array should be included afterward. Given [4,15,100] and [10,20,30,40], 
# return new array containing [4,10,15,20,30,40,100].

def zip(arr1, arr2):
    new_arr = []
    for i in arr1:
        new_arr.append(i)
    for i in arr2:
        new_arr.append(i)
    for n in range(len(new_arr)-1):
        for i in range(len(new_arr)-1-n):
            if new_arr[i] > new_arr[i+1]:
                new_arr[i], new_arr[i+1] = new_arr[i+1], new_arr[i]
    print(new_arr)

zip([5,7,1],[3,10,17])

# 4. Credit Card Validation (Bonus)
# The Luhn formula is sometimes used to validate credit card numbers. 
# Create the function isCreditCardValid(digitArr) that accepts an array of digits on the card 
# (13-19 depending on the card), and returns a boolean whether the card digits satisfy the Luhn formula, as follows:
# Set aside the last digit; do not include it in these calculations (until step 5);
# Starting from the back, multiply the digits in odd positions (last, third-to-last, etc.) by 2;
# If any results are larger than 9, subtract 9 from them;
# Add all numbers (not just our odds) together;
# Now add the last digit back in – the sum should be a multiple of 10.
# For example, when given digit array [5,2,2,8,2], after step 1) it becomes [5,2,2,8], then after step 2) it is [5,4,2,16]. 
# Post-3) we have [5,4,2,7], then following 4) it becomes 18. After step 5) our value is 20, so ultimately we return true. 
# If the final digit were any non-multiple-of-10, we would instead return false.