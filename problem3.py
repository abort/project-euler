import math
from fractions import gcd

def largest_prime(n):
	max_possible_prime_factor = math.floor(math.sqrt(n))
	possible_primes = filter(lambda x: n % x == 0, generate_primes_upto_number(max_possible_prime_factor)) # optimize by finding first prime factor, then by dividing the number by that prime factor and repeat the process on the result
	return max(possible_primes)


# generate up to a number or get the first prime
def generate_primes_upto_number(n):
	primes = [2, 3] # first prime
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

# only works for composite numbers
def largest_prime_old(n):
	# every composite number consists of a prime smaller than its square root
	factor = math.floor(math.sqrt(n))
	largest_prime = n
	while factor > 1:
		# simple check to prevent extra checks for composite numbers as factors
		if (is_possible_prime(factor)):
			# check if n is divisible by the factor and they share the same gcd
			# TODO: add check for primality
			if (n % factor == 0 and gcd(n, factor) == factor):
				# if they share the same gcd, they must consist of the same prime factors
				n = factor
				largest_prime = factor
				factor = math.floor(math.sqrt(factor))
		factor -= 1
	return largest_prime
	

def is_possible_prime(n):
	if (n in [2, 3, 5]): 
		return True
	if (n & 0x1 != 0): # every prime number > 7 is odd 
		if (n % 5 == 0): return False
		return True
	
	return False