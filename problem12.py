import math
from itertools import count
from functools import reduce

# minimum required factors
min_factors = 500

def problem12():
	return reduce(lambda x: n * (n + 1) // 2, x for n in count(1) if not has_enough_condition_factors(x))

def has_enough_condition_factors(n):
	return len(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)))) >= min_factors