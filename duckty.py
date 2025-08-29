### DUCK TYPING ->> Another way to achieve polymorphism besides inheritance 
### Object must have the minimum necessary attributes/methods 
### if it looks like a duck and quacks like a duck, it must be a duck.

class Animal: 
    alive = True 
    
class Dog(Animal): 
    def speak(self):
        print("WOOF!")
        
class Cat(Animal): 
    def speak(self):
        print("MEOW")
        
class Car: 
    alive = False 
    def speak(self):
        print("Honk!")
        
animals = [Dog(), Cat(), Car()]

for animal in animals: 
    animal.speak()
    print(animal.alive)