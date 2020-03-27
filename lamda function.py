def is_even(n):
    return n % 2 == 0


nums = [3, 2, 4, 7, 8, 44, 33, 12]
even = list(filter(is_even, nums))  # filter is a function that take two argument  at a time
print(even)
