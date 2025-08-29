### Nested Class ->> A class defined with in another class. example below. 
### class Outer 
###    class Inner 
### Benefits ->> Allows us to logically group classes that are closely related.  
### Encapsulates private details that are not relvant outside of outer the class.  
### Keeps the namespace clean, reduces the possibility of naming conflicts.  

class Company: 
    class Employee: ### nested class with its attributes below i.e with contructor and with get_details.  
        def __init__(self, name, position):
            self.name = name 
            self.position = position 
           
        def get_details(self):
            return f"{self.name} {self.position}"
          
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = [] 
        
    def add_employess(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)
        
    def list_employees(self):
        return [employee.get_details() for employee in self.employees]
    
    
company1 = Company("orhan")
company2 = Company("AIT Solutions")

company1.add_employess("Ali", "DevOps Engineer")
company1.add_employess("Murtaza", "Office Boy")
company1.add_employess("Babar", "Peon")

company2.add_employess("Harry", "Software Engineer")
company2.add_employess("Mehmet", "Admin")
company2.add_employess("William Kenedy", "Golang Expert/System Design Eng")

for employee in company1.list_employees():
    print(employee)
    
for employee in company2.list_employees():
    print(employee)

 