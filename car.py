class Car:
   def __init__(self, year, model, color, for_sale): ### creating the constructor for the Car 
       self.year = year 
       self.model = model 
       self.color = color 
       self.for_sale = for_sale
       
       
   def drive(self):
      print(f"you drive the {self.color} {self.model}")  ### self is refering to the object we are cuurently working on. and . is attribute access operator. self.color , followed by the name of the attribute. i.e color,model. 
      
   def stop(self):
      print(f"you stop the {self.color} {self.model}")
      
   def describe(self):
      print(f"{self.year}, {self.model}, {self.color}")