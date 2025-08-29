# @property ->> Decorator used to define a method as a property (it can be accessed like an attribute.)
# Benefit ->> adds additional logic when read write or delete attributes 
# Gives us getter setter and deleted method.  

# class Rectangle: 
#     def __init__(self,width,height):
#         self._width = width  # when we add _before the param then its becomes private. 
#         self._height = height  # when we add _before the param then its becomes private.  
        
#     @property ##getter method to access the priv val.  
#     def width(self):
#          return f"{self._width:.1f}cm"
     
#     @property ##getter method to access the priv val. 
#     def width(self):
#         return f"{self._height}"
    
#     @width.setter 
#     def width(self, new_width):
#         if new_width < 0:
#             self._width = new_width
#         else: 
#             print("Width must be greater than zero.")
            
    
#     @height.setter 
#     def height(self, new_height):
#         if new_height < 0:
#             self.height = new_height 
#         else: 
#             print("Height must be greater than zero.")
            
#     rectangle = Rectangle(3,4) 
    
# rectengle.width = 6 
# rectengle.height = 5 

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero.")

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero.")


# Usage
rectangle = Rectangle(3, 4)
rectangle.width = 6
rectangle.height = 5

print(rectangle.width)   # 6.0cm
print(rectangle.height)  # 5.0cm


        