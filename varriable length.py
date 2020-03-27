def sum(a, *b):  # *b is variable length argument so it can take multiple arrgument at a time
    c = 0
    for i in b:
        c = c + i
    print(c)


sum(5, 6, 34, 78)
