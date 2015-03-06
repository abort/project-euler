import math

sizes_to_twenty = {
	0: 0, # placeholder
	1: 3, # one
	2: 3, # two
	3: 5, # three
	4: 4, # four
	5: 4, # five
	6: 3, # six
	7: 5, # seven
	8: 5, # eight
	9: 4, # nine
	10: 3, # ten
	11: 6, # eleven
	12: 6, # twelve
	13: 8, # thirteen
	14: 8, # fourteen
	15: 7, # fifteen
	16: 7, # sixteen
	17: 9, # seventeen
	18: 8, # eighteen
	19: 8, # nineteen
}

prefixes_to_hundred = {
	20: 6, # twenty
	30: 6, # thirty
	40: 5, # forty
	50: 5, # fifty
	60: 5, # sixty
	70: 7, # seventy
	80: 6, # eighty
	90: 6  # ninety
}

def problem17():
	total_length = 0
	for i in range(1, 1001):
		total_length += get_digit_to_string_length(i)
	return total_length

def get_digit_to_string_length(n):
	assert(n <= 1000)

	if (n == 1000): # one thousand
		return 11

	add_and_infix = (n > 100 and n < 1000)
	description_length = 0
	skip_next = False
	while (n > 0):
		exponent = int(math.log(n, 10))
		dimension = 10 ** exponent
		multiplier = n // dimension

		# retrieve description length
		description_length += get_single_logarithmic_length(multiplier, exponent, add_and_infix, n, skip_next)
		n -= multiplier * dimension

		if (skip_next):	skip_next = False
		# we have to skip the next
		if (exponent == 1 and multiplier == 1):
			skip_next = True

	return description_length

def get_single_logarithmic_length(m, exponent, add_and_infix, n, skip):
	assert(exponent <= 2) # just need up to 10^2 as 10^3 is instantly 11
	length = 0

	if (exponent == 2): # hundred
		length += sizes_to_twenty[m] # prefix, one or two etc
		length += 7 # 7 for hundred 
		if (add_and_infix and (n % 100 != 0)): # and when theres something to and
			length += 3
	elif (exponent == 1):
		length = sizes_to_twenty[n] if (n < 20) else prefixes_to_hundred[m * 10]
	else:
		length = sizes_to_twenty[n] if (not skip) else 0

	return length