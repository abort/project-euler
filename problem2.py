# max accepted value :)
max_fibonacci = 4 * 10 ** 6

def problem2():
	return sum(fibonacci_sequence_with_conditions(stop_condition, sum_condition))

def stop_condition(term, number):
 	# not exceeding max_fibonacci
 	return (number > max_fibonacci)

def sum_condition(term, number):
	# found an error in the assignment: we are looking for even numbers, not even terms! ffs
	return (number % 2 == 0 and number <= max_fibonacci)

# just to learn generators, could use summing instantly and no need for generators
def fibonacci_sequence_with_conditions(stopConditionFunction, sequenceConditionFunction = None):
	i = 1
	lastFib = 0 # fib(n - 1)
	semiLastFib = 1 # fib(n - 2)
	while True:
		if (i == 1): newFib = 1
		elif (i == 2): newFib = 2
		else: newFib = lastFib + semiLastFib
		semiLastFib = lastFib # fib(n - 2) = fib(n - 1) as we gen a new number
		lastFib = newFib # fib(n - 1) = newly generated fib (fib(n))

		if (sequenceConditionFunction is None or sequenceConditionFunction(i, newFib)):
			yield newFib

		if (stopConditionFunction(i, lastFib)):
			break

		i += 1

# not too good for performance thus we use generators
def fibonacci(n):
	assert(n > 0)
	initialList = [1, 1]
	if (n <= 2):
		return initialList[n - 1]
	return fibonacci(n - 1) + fibonacci(n - 2)