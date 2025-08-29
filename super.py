### super() ->> Function used in the child class to call methods from a parent class (superclass).   
### Allows us to extend the functionality of the inherited methods.   

class Shape:
    def __init__(self, color, is_filled):
        self.color = color 
        self.is_filled = is_filled  
        
    ### to extend the functionality of methods
    def describe(self):
        print(f"it is {self.color} and {'filled' if self.is_filled else 'not_filled'}")
        
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled) ### thats how we use super func to inherit from the parent Class.   
        self.radius = radius 
        
    ### method overriding as there two describe methods so when we call describe it gonna use this one.  
    ### if a child shares a similar method with the parent, we will use the child version.  
    def describe(self):
        print(f"it is an circle with an area of {3.14 * self.radius * self.radius }cm^2")
        super().describe()
        
        
class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled) ### thats how we use super func to inherit from the parent Class.   
        self.width = width 
        
        
class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)  ### thats how we use super func to inherit from the parent Class.   
        self.width = width   
        self.height = height
        
circle = Circle("purple", True, 4) 
square = Square("Magenta", True, 3) 
triangle = Triangle("Orange", False, 10, 6)

# print(triangle.color)
# print(triangle.is_filled)
# print(triangle.width)
# print(triangle.height)


circle.describe()