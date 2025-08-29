### Inheritence = Allows a class to inherit objects and methods from another class.   
### Helps with code reusability and extensibility 
### class Child(Parent) also knows as Sub-class(Super-classes)


class Animal: 
    def __init__(self, name):
        self.name = name 
        self.is_alive = True 
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping badly.")
    
    
class Dog(Animal): ### making the sub-classes from the Main Animal class or inheriting from the Animal 
    def speak(self): ### methods as dog can bark as woof. 
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")

 
dog = Dog("Scooby")
cat = Cat("Lara")
mouse = Mouse("Jerry")


dog.speak()

