def prob_6():
    """ Difference of the sum of squares and square of sums up to 100.
    """
    
    def sum_of_squares(top):
        num_sum = 0
        for num in range(top + 1):
            num_sum += num ** 2
        
        return num_sum
            
            
    def square_of_sums(top):
        num_sum = 0
        for num in range(top + 1):
            num_sum += num
        
        return num_sum ** 2
            
        
    return abs(sum_of_squares(100) - square_of_sums(100))