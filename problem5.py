from functools import reduce
from operator import mul
import math
 
def problem5(max_divisor = 20):
        primes = generate_primes_upto_number(max_divisor)
        min_value = reduce(mul, primes)
 
        # we have every composite number of consisting of different primes
        # we now need the composite numbers consisting of one single prime
        extra_factors = []
        for p in primes:
                if (p > max_divisor): break
                c = p # composite number var
                while (c <= max_divisor):
                        # if it is not a divisor yet, add it
                        if (min_value % c != 0): extra_factors.append(p)
                        c *= p
 
        min_value *= reduce(mul, extra_factors)
        return min_value
 
# generate up to a number or get the first prime
def generate_primes_upto_number(n):
        primes = [2, 3] # first primes
        n -= 1
        current_number = primes[1]
        while current_number < n:
                current_number += 2
                square_root = math.floor(math.sqrt(current_number))
                prime = True
                for p in primes:
                        if p > square_root: break
                        elif current_number % p == 0:
                                prime = False
                                break
 
                if prime: primes.append(current_number)
        return primes