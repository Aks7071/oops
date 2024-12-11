class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f"This car is a {self.make} {self.model}.")

car1 = Car("Toyota", "Corolla")
car1.display_info()
