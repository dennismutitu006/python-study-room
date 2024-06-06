#a user defuned class can be defined as a generic class.
from logging import Logger

class LoggedVar[T]:
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('%s: %s', self.name, message)

#This syntax indicates that the class LoggedVar is parameterised around a single type variable T 
#This makes T valid as a type within the class body.
#Generic classes implicitly inherit from Generic. meaning for python 3.2 amd above you do 
#have to import the generic module but for version 3.1 < it is possible to inherit explicit
# from Generic to idicate a generic class:

from typing import TypeVar, Generic

T = TypeVar('T')

class LoggedVar(Generic[T]):
    ...
