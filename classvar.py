### class variables = shared among all instances of a class (instances=objects)
### defined outside of the constructor. 
### Allow you to share data among all objects created from that class. 
### its good practice to access the class variables with the created class.  

class Student: 
    
    class_year = 2023 ### class var defined outside the constructor 
    num_students = 0 ### class var now inside contructor we will access it by Class then class var instead of self which is for object/instances. 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1   
        
student1 = Student("Hasan", 30)
student2 = Student("Salman", 25)
student3 = Student("Candy", 22)
student4 = Student("Robinson", 24)



print(f"My Graduating class has {Student.num_students} students") ### printing through f string useful for string formatting in py. 
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
### print(Student.class_year) ### accessing class var with Class as its good practice to access class variables with the Class itself not with instances as we cant diffrenciate as its a class var or obj instance. 