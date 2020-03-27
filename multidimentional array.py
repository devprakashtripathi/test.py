from numpy import *

arr1 = array([
    [1, 2, 3, 4, 5, 6, 8],
    [4, 5, 6, 44, 55, 6, 4]
])
arr2 = arr1.flatten()  # convert into one dimention
# arr3 = arr2.reshape(2,2,4) #reshape
print(arr2)
