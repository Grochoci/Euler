def prob_2():
    """ Sum of the even-valued Fibonacci sequence values, that do not exceed 4 million.
    """
    
    f_seq = [1,2]
    num = 0
    num_sum = 0
    
    while num < 4000000:
        num = f_seq[-1] + f_seq[-2]
        f_seq += [num]
    
    for num in f_seq:
        if num % 2 == 0:
            num_sum += num
    
    return num_sum
    
    