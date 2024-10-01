"""

numpy:
List, dictionary, tupple

array, json, xml, csv

numpy in one of the python programming lib which helps you to work with multi dimensional array and you can perform advance mathemetical functions.

numpy help you to create array items

-list 

-> list supports multple data types
-> it should contain all the elements of same data type

->its not good with memory optimization
->its good with memory storing and optimization

when you have very mathematical complex calculations at that time you should use numpy

"""

import numpy as np
#if you want to access functions of lib then how to start
#name_of_package.

print(np.__version__)

array  = np.array([1,2,3,4,5,7])
print(array)
print(type(array))

#to access specific element

print(array[-1])

#slicing can be also used over here just like we did in list

#deleting works in numpy
array = np.delete(array,2)
print(array)

#2d array

my2dArray= np.array([[1,2,3,4,5,6,7,8,9],[34,78,90,90,87,67,23,67,80]])
print("---------------------------------------")
print(my2dArray.ndim)

print(my2dArray)
print(type(my2dArray))

print(my2dArray[0][8])
print(my2dArray[1][4])

#0d array
ZeroDArray = np.array(56)

#3d array

my3dArray = np.array([[1,2,3,4,5,6,7,8,9],[34,78,90,90,87,67,23,67,80],
                      [12,23,34,45,56,78,90,78,56]])

print(my3dArray)
print(my3dArray[2][3])



array1 = np.array([1,2,3,4])
array2 = np.array([6,8,9,2])

print(array1[1]*array2[3])

#data types in numpy

"""
i = integer
b = boolean
f = Float
S = string
O = object
"""

arr = np.array([1,2,34,5])
print(arr.dtype)


arr = np.array([1,2,34,5], dtype="S")
print(arr.dtype)

#myAns = arr[0]

#split which is being used for internal testing only

arrSplit = np.array([1,2,3,4,5,6,7,7,9,0])

output = np.array_split(arrSplit,3)
output[0]=5,9
print(output)

#search
#where functions will it give me single element multi element
print("---------------------------------------")
arr = np.array([1,2,34,5,34])
result = np.where(arr == 34)
print(result)

#todo => you need to take 1 to 10 array elements and
#you need to print even numbers from it using where functuion

#sort : you can use that to sort in A-Z or Z-A

newArray = np.sort(arr)
print(newArray)
myList = newArray.tolist()
print(type(myList))

#how to sort in reverese

reveresed_arr = newArray[::-1]
print(reveresed_arr)

print(newArray[::-1])

# : start from the beginning of array
# :-1 it will go from negative indexing

#filter: you want to see elements based on condition

array2 = np.array([23,67,89,90,34,67,90])
newarr = array2[array2 > 66]
print(newarr)



