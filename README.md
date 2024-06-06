#Python is a dynamically-typed language.
#Meaning that variable types are dynamically set at run time 
#Upon assignment of a value to a variable.
#e.g

def fn(a, b):
	return a + b

#Types of a and b are not known at build time only when a and b are assigned values 
#at run time.
Hence calling 
fn("a", 1)
	this will not raise an exception until the code is actually exec and the func
is called:
>>> fn("a", 1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str

In Python 3, type annotations do not change this. Python is still a dynamically-typed language. Type annotations serve the following purpose:

Code documentation: thanks to them, a developer reading type-annotated code (his own or someone else’s) will know exactly what type each variables is supposed to be. This helps reduce bugs and exceptions and accelerate the development cycle.
Linting and validation: code editors and continuous integration (CI) pipelines can be configured to automatically validate type-annotated code at build-time and catch bugs before they make it to production.
Copyright © 2024
