### Abstract class ->> A class that cannot be instantiated on its own, meant to be sub-classed.   
### They can contain abstract methods, which are declared but have no implementation.  
### Abstract classess benefits ->> 
### 1- Prevents Instantiation of the class itself.   
### 2- Requires children to use inherited abstract methods. 


from abc import ABC, abstractmethod

class Vehicle(ABC): ##passing abstract methods 
    @abstractmethod
    def go(self):
        pass
        
    @abstractmethod  ### to make use of use abstract method we first import it then use abstract method before our method. 
    def stop(self):
        pass
        
class Car(Vehicle):
    def go(self):
        print("you drive the car with keys.")
        
    def stop(self):
        print("you stopped the car.")

class Bike(Vehicle):
    def go(self):
        print("you ride the bike")
    
    def stop(self):
        print("you stop the bike with break")   

class Truck(Vehicle):
    def go(self):
        print("you races the 22 wheeler truck")
        
    def stop(self):
        print("you stopped the truck")
        
        
truck = Truck()

truck.go()
truck.stop()