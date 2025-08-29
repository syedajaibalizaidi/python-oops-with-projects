### Aggregation ->> A relationship where one object contains reference to other independent objects "has-a relationship"
### Composition ->> The composed object directly owns its components, which cannot exist independently. "owns-a realtionship" 

class Engine:
    def __init__(self,horse_power):
        self.horse_power = horse_power 

class Wheel: 
    def __init__(self,size):
        self.size = size 
        
class Car: 
    def __init__(self,make,model,horse_power,wheel_size):
        self.make = make   
        self.model = model
        self.engine = Engine(horse_power)  ### these are composed object as the car owns the engine and the wheels car directly owns engines and wheels.  
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]   ### these are composed object as the car owns the engine and the wheels 
    
    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power} {self.wheels[0].size}" ### thats how we access composed object here.  
    
car1 = Car("Ford", "BMW", 600, 13)
car2 = Car("Audi", "KIA", 777, 22)

print(car1.display_car())
print(car2.display_car())
        