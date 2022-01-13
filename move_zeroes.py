def move_zeros(list):
    for i in range(0,len(list)):
        if list[i] == 0:
            list.append(list[i]) #this will add index of i to the end of the list
            list.remove(list[i]) #this will remove index of i in it's current index
    return(list)

print(move_zeros([0,0,3,5,0,9,7]))