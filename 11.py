class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    def greet_child(self):
        print("Hello from Child!")
#Inheritance allows a class to inherit attributes and methods from another class.
child = Child()
child.greet()         # Output: Hello from Parent!
child.greet_child()   # Output: Hello from Child!
