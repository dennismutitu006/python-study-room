#Since type information about objects kept in containers cannot be statically inferred in a 
#generic way, many container classes in the standard lib support subscription to denote the expected types  of container elements.
from collections.abc import Mapping, Sequence

class Employee: ...

# Sequence[Employee] indicates that all elements in the sequence
# must be instances of "Employee".
# Mapping[str, str] indicates that all keys and all values in the mapping
# must be strings.
def notify_by_email(employees: Sequence[Employee],
                    overrides: Mapping[str, str]) -> None: ...


#Generic functions and classes can be parameterized by using type parameter syntax.

from collections.abc import Sequence

def first[T](l: Sequence[T]) -> T: #Function is generic over the typeVar "T"
    return l[0]

#Or by using the TypeVar factory directly:

from collections.abc import Sequence
from typing import TypeVar

U = TypeVar('U')                  # Declare type variable "U"

def second(l: Sequence[U]) -> U:  # Function is generic over the TypeVar "U"
    return l[1]
