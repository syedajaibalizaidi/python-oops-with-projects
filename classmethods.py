### Class methods = Allow operations related to the class itself.  
### Take cls as the first parameter, which represents the class itself.  

# Instance Methods ->> Best for operations on instance of the class (objects). 
# Static Methods ->> Best for utility functions that do not need access to class data.  
# Class Methods ->> Best for class-level data or require access to class itself.   

class Student: 
    
    count = 0 ##class variable 
    total_gpa = 0 #class variable 
    
    def __init__(self, name, gpa):
        self.name = name 
        self.gpa = gpa 
        Student.count += 1 
        Student.total_gpa += gpa 
     
     #INSTANCE METHODS    
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total Students: {cls.count}"
    
    @classmethod
    def get_avg_gpa(cls): ## here we cls i.e class instead of self which is for objects 
        if cls.count == 0:
            return 0 
        else: 
            return f"Avg gpa: {cls.total_gpa / cls.count:.2f}"
        
        
student1 = Student("Ali", 3.8)
student2 = Student("Shebaz", 3.5)
student3 = Student("Zain", 1.9)

print(Student.get_count())
print(Student.get_avg_gpa())