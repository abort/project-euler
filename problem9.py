import math

def problem9(n = 1000):
	assert(n > 0)
	boundary_a = n
	over_boundary = n ** 2
	for a in range(1, n):
		for b in range(a + 1, n):
			c_squared = a ** 2 + b ** 2
			if c_squared >= over_boundary: break
			c = math.sqrt(c_squared)
			if (a + b + c == n):
				return a * b * c
	return -1