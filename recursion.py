import sys

sys.setrecursionlimit(2000)  # setlimit
print(sys.getrecursionlimit())
i = 0


def greet():
    global i
    i += 1
    print("hello", i)
    greet()  # calling the function.


greet()
