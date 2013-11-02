def prob_5():
    """ Smallest positive Natural number that is evenly divisable by
    1 through 20.
    """
    
    num = 20
    divisor = 1
    
    while divisor < 21:
        if num % divisor == 0:
            divisor += 1
        else:
            num += 20
            divisor = 1
            
    return num