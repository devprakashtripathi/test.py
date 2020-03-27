def greet():
    print("hello")  # definition of the function
    print("good morning")
    greet()  # calling of the function


def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d  # return the value


result1, result2 = add_sub(5, 4)  # passing the argument
print(result1, result2)
