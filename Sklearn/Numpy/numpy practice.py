# -*- coding: utf-8 -*-
"""
Created on Wed May 11 17:55:43 2022

@author: TOBBY
"""

#To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))

#numpy version
print(np.__version__)


arr1 = np.array((1, 2, 3, 4, 5))
print(arr1)
print(type(arr1))



arr2 = np.array([1,2,3,4,5,6,7,8])
print(arr2)


#creating a zero dimensional array with 42 as the value
arr3 = np.array(42)
print(arr3)

#An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array. These are the most common and basic arrays
arr4 = np.array([1,2,3,4,5,6])

#an array that has 1D arrays as its elements is known called a 2-D array
#these are used to create a 2nd order tensors
# the two dimensions must have the same number of elemnts or it will return a visibledepreciatedwarning error
arr5 = np.array([[1,2,3,4,5,6], [10,20,30,40,40,60]])
print(arr5)

print('\n')


#3D
arr6 = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])
print(arr6)

print('\n')

arr7 = np.array([[[10,20,30], [40,50,60]], [[10,20,30], [40,50,60]]])
print(arr7)

print('\n')

arr8 = np.array([[[2,4,6],[8,8,8]], [[2,4,6], [8,8,8]]])
print(arr8)

print('\n')

arr9 = np.array([[[5,5,5, 11],[2,2,2,8]], [[5,5,5,11], [2,2,2,8]]])
print(arr9)

print("\n")

a = np.array(120)
b = np.array([1,2,3,4,5,6])
c = np.array([[2,4,7], [7,8,11]])
d = np.array([[[1,3,5], [2,8,8]], [[1,3,5], [2,8,8]]])
e = np.array([[[[1,7,9],]]])
f = np.array([[[[[1,2,3], [2,4,6]], [[1,2,3], [1,2,3]], [[1,2,3], [1,2,4]]]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print(e.ndim)
print(f.ndim)

#the number of square brackets is one of the foremost things that determine the number of dimensions of the array
arr10 = np.array([1,2,3,4,5], ndmin=5)
print(arr10)
print(type(arr10))

print('\n')

#32 is the highest allowable number of dimensions using ndmin
arr11 = np.array([2,4,6,8,20], ndmin=32)
print(arr11)
print('number of dimensions: ', arr11.ndim)


arr12 = np.array([[20,40,60,80]], ndmin=2)
print(arr12)
print("the number of dimensions are:", arr12.ndim)
for i in arr12:
    print(type(i))


#array indexing is the same as accessing an array, you can access an array element by referring to its index numbers
arr13 = np.array([1,2,3,4,5,6])
print(arr13[1])
print(type(arr13[1]))

arr14 = np.array([10,20,30,40,50])
print(type(arr14[2]))
print(arr14[0] + arr14[2])
print(arr14[1])
print(arr14[2])
print(arr14[3])
print(arr14[4])

sum_of_elements = arr14[0] + arr14[1] + arr14[2] + arr14[3] + arr14[4]
print(sum_of_elements)

for i in arr14:
    print(i + arr14)

print("\n")

print(sum_of_elements + arr)

print("\n")

#get the third and fourth element then add them
arr15 = np.array([1, 2, 3, 4])
print("the third element of the array is: ",  arr15[2], "while the fourth element is: ", arr15[-1])
print("sum of third and fourth element is: ", arr15[2] + arr15[-1])

#accessing 2-D arrays
#To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.
#Think of 2-D arrays like a table with rows and columns, where the row represents the dimension and the index represents the column.

arr16 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("the third element in the 2nd row is: ", arr16[1,2])

arr17 = np.array([[1,5],[10,15]])
print(arr17[1,1])

#access 3-D arrays
arr18 = np.array([[[2,4,6,8,10],[12,14,16,18,20]], [[22,24,26,28,30], [32,34,36,38,40]]])
print("the third elemnt in the second array of the first array is", arr18[0,1,2])


arr19 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("the last element from the second dimension is:", arr19[1, -1])


#Slicing arrays
#Slicing in python means taking elements from one given index to another given index.
""" We pass slice instead of index like this: [start:end].
We can also define the step, like this: [start:end:step].
If we don't pass start its considered 0
If we don't pass end its considered length of array in that dimension
If we don't pass step its considered 1"""


arr20 = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr20[1:5])
print(arr20[4:]) #print from index 4 to the end of the array
print(arr20[:4]) #print from the starting index to index 4

#Negative slicing
#use the minus operator to slice from index 3 from the end to index 1 from the end
arr21 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr21[-3:-1])
print(arr21[-3*-1], arr21[-3:-1])
print(arr21[1::-1]) #that is print index 1 slice everything until you get to the index before index 1

arr22 = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr22[1:5:2]) #print from index 1 to 5 but take 2 steps while moving through index 1 to 5, the last : at the end modifies the step to take when printing an index ion the array
print(arr22[::2])

#print the odd numbers out of the array [1,2,3,4,5,6,7,8,9,10,11,12]
arr23 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr23[:11:2]) #it automatically assumed the blank place is 0, that is before the :11
print(arr23[1:11:2]) #to print out the even numbers

#slicing 2-D arrays
arr24 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr24[1, 1:4]) #to symbolise the element we are slicing from, we use 1, for index 1 to get the second element in the dimension
print(arr24[1, 1:4:2]) #this will print the numbers in the 2nd element starting from its index 1 and taking 2 steps
print(arr24[0:2, 2::-2]) #:: is used to reverse an array, the 2 means ignore 2 and start from 3 while printing in a reverse form taking 2 steps from the back
print(arr24[0:2, -1:2:-1])   #to print out 5, and 10,9 respectively
print(arr24[0:2, -2::-2]) #to print out 4,2 and 9,7 respectively from both elements
print(arr24[0:2, -3::-2]) #print out 3,1 and 8,6 respectively from both elements
print(arr24[0:2, 3::-3]) #prints out 4,1 and 9,6 respectively
print(arr24[0:2, -2])
print("the product of the first two elements in each dimension is: ", arr24[0, 0:2] * arr24[1, 0:2]) #do 1,2 * 6*7 to print 6,14
print("the product of the last two elements in both dimension are: ", arr24[0, 4:2:-1] * arr24[1, 4:2:-1])

arr25 = np.array([10, 15, 20, 25, 30, 35, 40])
print(arr25[1:4])

#NumPy datatypes

""" i - integer
    b - boolean
    u - unsigned integer
    f - float
    c - complex float
    m - timedelta
    M - datetime
    O - object
    S - string
    U - unicode string
    V - fixed chunk of memory for other type ( void )"""
#The NumPy array object has a property called dtype that returns the data type of the array

arr26 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr26.dtype)

arr27 = np.array(["cherry", "strawberry", "mangoes", "apple", "oranges"])
print(arr27.dtype)

arr28 = np.array([1,2,3,4,5,6,7], dtype = 'S')
print(arr28)
print(arr28.dtype)    

arr29 = np.array([1,2,3,4], dtype='i4')
print(arr29)
print(arr29.dtype)

arr30 = np.array([1,2,3], 'i')
print(arr30)


#converting data type on existing arrays
arr31 = np.array([1.1, 2.1, 3.1, 4.1, 4.5])
newarr31 = arr31.astype('i')
print(newarr31)
print(newarr31.dtype)
print(arr31.dtype)


#Change data type from float to integer by using int as parameter value
arr32 = np.array([1.1, 2.1, 3.1])
newarr32 = arr32.astype(int)
print(newarr32)
print(newarr32.dtype)

#Change data type from integer to boolean
arr33 = np.array([1, 0, 3])
newarr33 = arr33.astype(bool)
print(newarr33)
print(newarr33.dtype)
print(arr33)
print(type(arr33),'datatype is: ', arr33.dtype) 

arr34 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newarr34 = arr34.astype(float)
print(newarr34)
print(newarr34.dtype)

# the type() class will return the type of array while the dtype reference will return the type of data in that array

arr35 = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr35[0] = 42
print(arr35)
print(x)

arr36 = np.array([2,4,5,8,10])
a = np.zeros((4,4))
print(a)





















































