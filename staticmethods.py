### Static Methods ->> A method that belong to a class rather than any object from that class (Instance).
### Usually used for general utility functions. 

### Instance Methods ->> Best for Operations on instances of the class (objects).  
### Static Methods ->> Best for Utility functions that do not need access to class data.  

### for an instance method we access an object and call the instance method.  
### with the static method we only need to access that class and we dont need to create any object from that class.  

class Employee: 
    def __init__(self, name, position):
        self.name = name 
        self.position = position  
        
    def get_info(self):
        return f"{self.name} = {self.position}" 
    
    @staticmethod ### static methods 
    def is_valid_position(position): 
        valid_positions = ["Manager", "CEO", "Janitor", "Peon"]
        return position in valid_positions
    
employee1 = Employee("Waseem Dabbu", "Janitor") ### instance method accessing object via instance method. 
employee2 = Employee("Shebaz", "Manager") ### instance method accessing object via instance method. 
employee3 = Employee("Ali Zaidi", "CEO") ### instance method accessing object via instance method. 
employee4 = Employee("Yasir Bona", "Sweeper") ### instance method accessing object via instance method. 

print(Employee.is_valid_position("Peon")) # with the static method we only need to access that class and we dont need to create any object from that class. as we did here.  
print(employee1.get_info())  # for an instance method we access an object and call the instance method. as we did here. 
print(employee4.get_info())  # for an instance method we access an object and call the instance method. as we did here.

