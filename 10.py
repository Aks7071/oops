#encapsulation
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute
    
    def get_age(self):
        return self.__age  # Access through a method
    
    def set_age(self, age):
        if age > 0:
            self.__age = age
#Encapsulation refers to the bundling of data and methods into a single unit,
person = Person("John", 30)
print(person.get_age())  # Output: 30
person.set_age(35)
print(person.get_age())  # Output: 35
