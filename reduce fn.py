from functools import reduce  # it reduce the value

nums = [3, 2, 4, 6, 8, 9, 2, 7, 8]
evens = list(filter(lambda n: n % 2 == 0, nums))
doubles = list(map(lambda n: n * 2, evens))
print(doubles)
sum = reduce(lambda a, b: a + b, doubles)
print(sum)
