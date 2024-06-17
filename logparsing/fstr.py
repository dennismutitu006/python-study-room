'''
f-strings let u include the value of py expressions inside a strings by prefixin 
with f or F and writing expressions as {expression}.
An optional format specifier can follow the expression. This allows greater control
over the vakue being formatted.
'''
# ex of rounds pi in 3 dp

import math
print(f'The value of pi is approximately {math.pi:.3f}.')
#The value of pi is approximately 3.142.

#Passing an integer after the ':' will cause that field to be a minimum number of
#characters wide hence useful for making columns line up

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
'''Result
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
'''

#other modifiers to convert values before its formatted '!a' for ascii()
#!r for repr() and !s 4 str()
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels. #result
print(f'My hovercraft is full of {animals!r}.')
"""My hovercraft is full of 'eels'."""

#the = specifier can be used to expand an exp to the text of the expression

bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')
"""expected results
Debugging bugs='roaches' count=13 area='living room'
"""
