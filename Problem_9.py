from math import sqrt

def prob_9():
    """ There is one Pythagorean triplet for which a + b + c = 1000, find the product of abc.
    """
    
    # a <= 332, b <= 499 ---- Not possible anyways but start point
    # (a ** 2) + (b ** 2) = (c ** 2)
    # a + b + c = 1000
    
    a = 1
    
    while a < 332:
        b = a + 1
        while b < 500:
            c = (a ** 2) + (b ** 2) 
            if (sqrt(c) - int(sqrt(c))) == 0:
                if (a + b + (sqrt(c))) == 1000:
                    return a * b * (sqrt(c))
            b += 1
        a += 1