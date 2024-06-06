#For most containers in Python, the typing system assumes that all elements in the container# will be of the same type. e.g
from collections.abc import Mapping

# Type checker will infer that all elements in ``x`` are meant to be ints
x: list[int] = []

# Type checker error: ``list`` only accepts a single type argument:
y: list[int, str] = [1, 'foo']

# Type checker will infer that all keys in ``z`` are meant to be strings,
# and that all values in ``z`` are meant to be either strings or ints
z: Mapping[str, str | int] = {}
# Mapping only accepts two type arguments: the first indicates the type of
#the keys, and the second indicates the type of the values.
