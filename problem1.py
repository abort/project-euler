def problem1():
	multiplesOfFive = { x * 5 for x in range(1, 999 // 5 + 1) }
	multiplesOfThree = { x * 3 for x in range(1, 999 // 3 + 1) }
	unionOfMultiples = multiplesOfFive.union(multiplesOfThree);
	return sum(unionOfMultiples)