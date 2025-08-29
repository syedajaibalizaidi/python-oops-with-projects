### Polymorphism -> Greek word to have many forms and faces.   
### Poly ->> Means Many , Morphe ->> Means Form 
### Two ways to achieve polymorphism 
### 1- INHERITENCE ->> An object could be treated of the same type as a parent class 
### 2- Duck Typing ->> Object must have necessary attributes and methods.   

from abc import ABC, abstractmethod

class Shape: 
    @abstractmethod ### using the abstract method. adding the decorator of the abstract method. 
    def area(self): 
        pass 


class Circle(Shape): 
    def __init__(self, radius):
        self.radius = radius 
        
    def area(self):
        return 3.14 * self.radius ** 2 


class Square(Shape): 
    def __init__(self, side):
        self.side = side 
        
    def area(self):
        return self.side ** 2 

class Triangle(Shape): 
    def __init__(self, base, height):
        self.base = base 
        self.height = height 
        
    def area(self):
        return self.base * self.height * 0.5 

class Pizza(Circle): 
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping 

### pizza here is good example of polymorphism as it is circle and circle is of shape so it has three forms.  
shapes = [Circle(3), Square(4), Triangle(6,7), Pizza("cheese boti", 12)] ## passing the list of the shapes as they all have shapes in common inherit from shapes but pizza is of circle type so will inherit from circle.   


for shape in shapes: 
    print(f"{shape.area()}cm")