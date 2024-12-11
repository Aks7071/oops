#polymorphism
class Dog:
    def speak(self):
        return "Woof!"
    
class lion :
    def speak(self):
        return "awww!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_speak(animal):
    print(animal.speak())
#creating object
dog = Dog()
cat = Cat()
lion=lion()

animal_speak(dog)  # Output: Woof!
animal_speak(cat) # Output: Meow!
animal_speak(lion) #imp is speak method is called  in the project