class Employee:
    holidays=["New Year"]
    def __init__(self,id,dept,salary):
        self.id=id
        self.dept=dept
        self.salary=salary
    def get_tax(self): #instance-level method
        return 0.3*self.salary
    @classmethod
    def get_holiday(cls): #class-level method 
        return cls.holidays
    
emp1=Employee(1,"AB",10)
emp2=Employee(3,"gh",100)
print(emp1.get_tax())
print(emp2.get_tax())
print(Employee.get_holiday())
print(emp1.get_holiday())
print(emp2.get_holiday())