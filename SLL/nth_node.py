def solution(numbers, left, right):
    array = []
    for i in range(len(numbers)):
        # compute x=numbers[i]/(i+1)
        # if left <= x <= right then array[i]=true, else array[i] = false
        x = float(numbers[i])/float((i+1))
        print(x)
        if x >= left and x <= right:
            # numbers[i] == True
            array.append(True)
        else:
            # numbers[i] == False
            array.append(False)
        
    return array

print(solution([8, 5, 6, 16, 5], 1, 3))

# Input:
# numbers: [8, 5, 6, 16, 5]
# left: 1
# right: 3

# Input:
# numbers: [65, 46, 60, 164, 243, 228, 231, 298, 231, 211]
# left: 20
# right: 50
# Output:
# [false, true, true, true, true, true, true, true, true, true]
# Expected Output:
# [false, true, true, true, false, true, true, false, false, false]

# Only solved 1/16 hidden tests




sentence = "the bird and the dog are loud"
words = ['cat', 'dog']

[5,2]
