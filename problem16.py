import math

# exponent
def problem16(e = 1000):
	n = 2 ** e
	s = 0
	while (n > 0):
		subtract = int(math.log(n, 10))
		dimension = 10 ** subtract
		multiplier = n // dimension
		s += multiplier
		n -= multiplier * dimension

	return s

def problem16_slow(e = 1000):
	return sum(list(map(int, list(str(2 ** e)))))