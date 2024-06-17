'''Diff b2n str() and repr()'''
#The str() is meant to return representations of values which are fairly human
#Readable while repr() generates reps which can be read by the interpreter.
#For objects which don’t have a particular representation for human consumption, 
#str() will return the same value as repr()

'''string representations example'''

s = 'Hello, world.'
str(s)
'Hello, world.'
repr(s)
"'Hello, world.'"

str(1/7)
'0.14285714285714285'
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
The value of x is 32.5, and y is 40000...
# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
'hello, world\n'
# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
