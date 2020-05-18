"""
Abstract classes are classes that contain one or more abstract methods.
An abstract method is a method that is declared, but contains no implementation.
Abstract classes cannot be instantiated, and require subclasses to provide
implementations for the abstract methods.

Python doesn't provide abstract class, Python has a module which provide 
abstract class

"""

 
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def do_something(self):
        pass


class DoAdd(AbstractClass):
    def do_something(self):
        print(self.value + self.value)


class DoMul(AbstractClass):
    def do_something(self):
        print(self.value * self.value)


obj1 = DoAdd(2)
obj1.do_something()

obj2 = DoMul(2)
obj2.do_something()
