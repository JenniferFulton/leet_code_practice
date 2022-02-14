# 1. Multiples of Three – but Not All
# Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.
for i in range(-300,0,3):
    if i != -6 and i != -3:
        print(i)

# 2. Printing Integers with While
# Print integers from 2000 to 5280, using a WHILE.
x = 2000
while x >= 2000 and x <= 5280:
    print(x)
    x += 1

# 3. Counting, the Dojo Way
# Print integers 1 to 100. If divisible by 5, print "Coding" instead. 
# If by 10, also print " Dojo".
for y in range(1,100):
    if y % 5 == 0:
        print ('Coding')
    if y % 10 == 0:
            print('Dojo')

# 4. Flexible Countdown
# Based on earlier “Countdown by Fours”, given lowNum, highNum, mult, print 
# multiples of mult from highNum down to lowNum, using a FOR. For (2,9,3), 
# print 9 6 3 (on successive lines).
def countdown(lowNum, highNum, mult):
    for i in range(highNum, lowNum, (mult*-1)):
        print(i)

countdown(2,9,3)