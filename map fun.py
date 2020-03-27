# double all values
nums = [12, 4, 5, 66, 88, 8, 2, 6]
evens = list(filter(lambda n: n % 2 == 0, nums))  # double onley the evens no
double = list(map(lambda n: n * 2, evens))
print(double)
