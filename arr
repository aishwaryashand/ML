#!/usr/bin/python3

import numpy
i = int(input("Enter number of rows: "))
j = int(input("Enter number of columns: "))
k = int(input("Enter repetitive value of array: "))
print("no. of rows= ",i)
print("no. of column= ",j)
print("repetitive value= ",k)
ar1 = numpy.full((i,j),k)
print("The array will be: ")
print(ar1)
print("More possible combinations are:")
print(ar1.reshape(j,i))
