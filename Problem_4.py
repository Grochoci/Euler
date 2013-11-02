def prob_4():
    """ Largest Palindrom product of 2, 3 digit numbers.
    """
    
    largest = 0
    
    for num_1 in range (999, 100, -1):
        for num_2 in range (999, 100, -1):
            product = num_1 * num_2
            if str(product) == str(product)[::-1]:
                if product > largest:
                    largest = product
    
    return largest