def lonelyinteger(a):
    if len(a) == 1:
        return a[0]
    else:
        for i in a:
            if a.count(i) == 1:
                return i 
