# Recurive Fibonacci
# Write a recursive fnction that will display the value of the Fibonacci sequence at a given point(int)
# 1,1,2,3,5,8,13
# EX: 6 should return 8 

def recursiveFib(int):
    # int is the nth fib number
    if int == 2 or int == 1:
        return 1
    return recursiveFib(int-2) + recursiveFib(int-1)

print(recursiveFib(20))

# Recursive Sigma
# Write a recursive function that given a number returns the sum of integers from 1 to that number. 
# Example: rSigma(5) = 15 (1+2+3+4+5); rSigma(2.5) = 3 (1+2); rSigma(-1) = 0.


# Recursive Factorial
# Given num, return the product of ints from 1 up to num. If less than zero, treat as zero. 
# If not an integer, truncate. Experts tell us 0! is 1. rFact(3) = 6 (1*2*3). Also, rFact(6.5) = 720 (1*2*3*4*5*6).

