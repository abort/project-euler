def problem6(n = 100):
        square_of_sum = ((n * (n + 1)) // 2) ** 2
        sum_of_squares = (n * (n + 1) * (2 * n + 1)) // 6
        # or use:
        # sum_of_squares = sum(map(lambda x: x ** 2, range(1, n + 1)))
        return square_of_sum - sum_of_squares