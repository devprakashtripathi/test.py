from numpy import *

arr1 = array([5, 10, 15, 20, 30])
arr2 = array([55, 16, 1, 280, 60])
arr3 = ([])
k = 0
for num1 in arr1:
    num3 = num1 + arr2[k]
    arr3.append(num3)
    k += 1
print(arr3)
