# Pro/g/ramming Challenge Problem 14
# Collatz Conjecture

# From Wikipedia:
"""
Take any natural number n. If n is even, divide it by 2 to get n / 2. 
If n is odd, multiply it by 3 and add 1 to obtain 3n + 1. Repeat the process indefinitely. 
The conjecture is that no matter what number you start with, you will always eventually reach 1.
"""


def collatzRecursive(positiveInt, toPrint):
    # positiveInt only needs to be an integer in the 
    # mathematical sense, so longs are also fine
    assert positiveInt > 0
    assert type(positiveInt) == int or type(positiveInt) == long
    
    if toPrint:
        print positiveInt
    
    if positiveInt == 1:
        return 1
    elif positiveInt%2 == 0:
        return collatzSim(positiveInt/2, toPrint)
    else:
        return collatzSim(positiveInt*3 + 1, toPrint)
        
# Function TODO List
# Collatz Simulator which returns a list containing 
#   the number's path
# Test conjecture for large range of numbers
# Graph convergence times for multiple numbers in a series
# Graph convergence path for a single number
