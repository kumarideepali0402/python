class Employee():
    def __init__(self,id,dept,salary):
        self.id=id
        self.dept=dept
        self.salary=salary
    def get_tax(self): #method
        return 0.3*self.salary
emp1=Employee(1,"AB",10)
emp2=Employee(3,"gh",100)
print(emp1.get_tax())
print(emp2.get_tax())