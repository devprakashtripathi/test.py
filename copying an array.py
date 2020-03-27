from numpy import *

arr1 = array([2, 6, 8, 1, 3])
arr2 = arr1.view()  # function help to create new array for copy so it is called shallow copy
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
