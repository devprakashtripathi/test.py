av = 10
x = int(input("HOW ANY CANDIES DO YOU WANT ?"))
i = 1
while i <= x:
    if i > av:
        print("out of stock")
        break
    print("candy")
    i += 1

print("bye")
