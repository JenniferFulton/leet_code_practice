def subtractOne(array):
    #starting all the way to the right of the array
    index = len(array)-1

    while index >= 0 and array[index]==0:
        array[index] = 9
        index -= 1
    
    if index >= 0:
        array[index] -= 1

    if array[0] == 0:
        array.pop(array[0])

    return array
        


print(subtractOne([0]))
#print(subtractOne([1,2,0,0]))
#print(subtractOne([1,0,8]))




