# pro/g/ramming challenge #54

# Evaluate Binomial Coefficients

# The formula for binomial coefficients is:
#       n!
#    --------
#    k!(n-k)!

# It is the coefficient of the x^k term in the
# polynomial expansion of the binomial power (1 + x)^n

def fact(naturalNum):

    assert naturalNum > -1
    assert type(naturalNum) == int or type(naturalNum) == long
    
    if naturalNum == 0 or naturalNum == 1:
        return 1
    else:
        return naturalNum*fact(naturalNum-1)
        
def coeffCalc(n, k):
    
    return fact(n)/(fact(k)*fact(n - k))
    
