# so avoiding to the function we only use lambda
nums = [21, 5, 4, 7, 8, 12, 4, 7, 36, 48, 25, 12, 14, ]
evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)
