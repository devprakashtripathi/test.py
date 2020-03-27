from array import *

arr = array('i', [])
n = int(input("Enter the length of the array?"))
for i in range(n):
    x = int(input("Enter the value"))
    arr.append(x)
print(arr)
vals = int(input("Enter the value for search"))
print(arr.index(vals))  # this is in built function that return the index of element and we not use the loops.

# k = 0
# for e in arr:
# if e == vals:
# print(k)
# break
# k+=1
