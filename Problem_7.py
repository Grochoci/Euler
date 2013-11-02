from math import sqrt

def prob_7():
    """ Find out the 10 001st prime number.
    """
    
    prime_count = 6
    num = 13
    
    while prime_count != 10001:
        num += 2
        divisor = 3
        while divisor < int(sqrt(num) + 1):
            if num % divisor == 0:
                divisor = num
            elif (divisor + 2) > int(sqrt(num)):
                    prime_count += 1
                    divisor += 2
            else:
                divisor += 2
    
    return num