class Employee:
    CompanyName = "Apple"
    NoofEmployee = 0

    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.NoofEmployee +=1

    def showdetail(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.NoofEmployee} sized {self.CompanyName} is {self.raise_amount}")



emp1 = Employee("Umer")
emp1.raise_amount = 0.04
emp1.CompanyName = "Apple Pak"
emp1.showdetail()

emp2 = Employee("Zohaib")
emp2.CompanyName = "Google"
emp2.showdetail()