def person(name, **data):
    print(name)
    for i, j in data.items():
        print(i, j)


person('dev', age=23, city='Delhi', mob=7905386617)
