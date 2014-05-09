# Pro/g/ramming Challenge Problem 14
# Collatz Conjecture

# From Wikipedia:
"""
Take any natural number n. If n is even, divide it by 2 to get n / 2. 
If n is odd, multiply it by 3 and add 1 to obtain 3n + 1. Repeat the process indefinitely. 
The conjecture is that no matter what number you start with, you will always eventually reach 1.
"""

import pylab

# Note that python's default maximum recursion depth is 1000

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
        return collatzRecursive(positiveInt/2, toPrint)
    else:
        return collatzRecursive(positiveInt*3 + 1, toPrint)

def collatzIterative(positiveInt, toPrint):
    """
    Input: positiveInt - Postitive integer or long
    toPrint - if True, prints path as it's being taken
    
    Output: List showing the convergence path
    """        
    assert positiveInt > 0
    assert type(positiveInt) == int or type(positiveInt) == long
    
    convergencePath = []
    
    while positiveInt != 1:
        
        convergencePath.append(positiveInt)
        
        if toPrint:
            print positiveInt
            
        if positiveInt%2 == 0:
            positiveInt /= 2
        else:
            positiveInt = positiveInt*3 + 1
            
    return convergencePath
    
def collatzTest(numList, debug):
    """
    Input: numList - List of positive integers or longs
        debug - prints number trajectory mid-program
    Output: convergenceList - List of tuples (num, convergence time)
    """
    
    assert type(numList) == list
    convergenceList = []
    
    for i in numList:
        convergenceList.append((i, len(collatzIterative(i, False))))
        if debug:
            print convergenceList[-1]
        
    return convergenceList
    
def collatzPathGraph(positiveInt):
    """
    Graphs the path the number takes on the y-axis
    with the step number on the x-axis
    
    Input: positiveInt - Starting point for collatz path
    """
    
    pylab.plot(collatzIterative(positiveInt, False))
    pylab.title("Collatz Path for %s" % positiveInt)
    pylab.ylabel("Number at Collatz step")
    pylab.xlabel("Collatz step")
    pylab.show()
    
# Function TODO List
# Graph convergence times for multiple numbers in a series
