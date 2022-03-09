# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

def fizz_buzz(n):
    array = []
    for i in range(1,n+1,1):
        if  i % 3 == 0 and i % 5 == 0:
            array.append("FizzBuzz")
        elif i % 3 == 0:
            array.append("Fizz")
        elif i % 5 == 0:
            array.append("Buzz")
        else:
            array.append(str(i))
        
    return array

print(fizz_buzz(15))

#O(n) because it is only going through the range one time. It compares i to each if/elif/else statement during the iteration