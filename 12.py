from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth

rect = Rectangle(5, 4)
print(rect.area())  # Output: 20
#Abstraction is the process of hiding the implementation
# details of a class and exposing only the functionality.