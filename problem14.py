# n = even number upperboundary 
def problem14(n = 1000000):
	max_count = (0, 0)
	for n in range(n - 1, 1, -2): # only have to check uneven numbers :)
		count = sequence(n)
		if (count > max_count[0]):
			max_count = (count, n)
	return max_count[1]

def sequence(n):
	if (n <= 1):
		return 0
	return (1 + ((sequence(n // 2) if (n % 2 == 0) else sequence(3 * n + 1))))