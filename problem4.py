import math
import time

def problem4():
	three_digit_factors = range(999, 99, -1)
	max_palindrome = 0

	for i in three_digit_factors:
		for j in range(i, 99, -1): # we dont need to test for higher digits anymore
			value = i * j
			if (value % 10 == 0 or value < 10 or value <= max_palindrome): continue

			value_str = str(value)
			if (value_str[::-1] == value_str and value > max_palindrome):
				max_palindrome = value

	return max_palindrome