#Python runtime does not enforce function and variable type annotations.
#They can be used by third party tools such as type checkers, IDEs, linters, etc.
#this module provides runtime support for type hints
#e.g

def moon_weight(earth_weight: float) -> str:
    return f'On the moon, you would weigh {earth_weight * 0.166} kilograms.'

#the function takes an arg expected to be a float and is expected to return 
# an instance of str
