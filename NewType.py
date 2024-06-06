#Use the NewType helper to create distinct types:

from typing import NewType

UserId = NewType('UserId', int)
some_id = UserId(524313) #This does not create a new class just a regular function call.

#The static type checker will treat the new type as if it were a subclass of the original type.
#This is useful in helping catch logical errors:

def get_user_name(user_id: UserId) -> str:
    ...

# passes type checking
user_a = get_user_name(UserId(42351))

# fails type checking; an int is not a UserId
user_b = get_user_name(-1)

# 'output' is of type 'int', not 'UserId'
output = UserId(23413) + UserId(54341)

#the expression some_value is Derived(some_value) is always true at runtime.
#It is invalid to create a subtype of Derived:

from typing import NewType

UserId = NewType('UserId', int)

# Fails at runtime and does not pass type checking
class AdminUserId(UserId): pass

#it is possible to create a NewType based on a ‘derived’ NewType:

from typing import NewType

UserId = NewType('UserId', int)

ProUserId = NewType('ProUserId', UserId)
#and typechecking for ProUserId will work as expected.
