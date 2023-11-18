#python

def is_prime(n):
    for i in range(2, n):
        # be divided with no remainder, i is the factor of n, n is not prime number.
        if n % i == 0: 
            return False
    return True # n is prime number.

print(is_prime(5))