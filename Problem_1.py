def prob_1():
    """ Sum of all Natural numbers below 100 that are
    multiples of 3 and 5.
    """
    
    num_sum = 0
    for num in range(1000):
        if (num % 3 == 0) or (num % 5 == 0):
            num_sum += num
    return num_sum