#!/usr/bin/env python3
#Python program to demonstrate working of method1 and method2
rows, cols = (5, 5)
#method 2 1st approach
arr = [[0]*cols]*rows
#lets change the 1st element of the 1st row to 1 and print the array
arr[0][0] = 1

for row in arr:
    print(row)
#method 2 2nd approach
arr = [[0 for i in range(cols)] for j in range(rows)]

#again in this new array lets change the first element of the 1st row
#to 1 and print the array
arr[0][0] = 1
for row in arr:
    print(row)
