def countApplesAndOranges(s, t, a, b, apples, oranges):
    # s to t is the house
    # the apple tree is to the left of the house (a)
    # the orange tree is to the right of the house (b)
    # the apple lands d units from the tree (neg is to the left)
    
    #number of apples & oranges that will hit the house
    house_apples = 0
    house_oranges = 0
    
    for i in apples:
        apple_fell = i + a
        if apple_fell >= s and i <= t:
            house_apples += 1
    
    for i in oranges:
        orange_fell = i + b
        if orange_fell >= s and i <= t:
            house_oranges += 1
            
    print(house_oranges, house_oranges)

countApplesAndOranges(7,10,4,12,[2,3,-4],[3,-2,-4])