def prob_3():
    """ Largest Prime Factor of a number.
    """
    
    num = 600851475143
    factors = []
    factor = 2
    
    while num > 1:
        while num % factor == 0:
            factors.append(factor)
            num /= factor
        factor += 1
        if factor ** 2 > num:
            if num > 1:
                factors.append(num)
                break
    
    return max(factors)
        