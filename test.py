def pangrams(s):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for i in s:
        alpha.append(i)
    
    for j in alpha:
        if alpha.count(j) == 1:
            return("not pangram")
    
    return("pangram")

print(pangrams())
