class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showdetail(self):
        print(f"The id of the Employee is: {self.id} \n The name of Employee is: {self.name}")


class Language(Employee):
    def my_language(self):
        print("I am the python language Expert...")

e1 = Employee("Umer", 35)
e1.showdetail()
e2 = Language("Nawaz", 47)
e2.showdetail()
e2.my_language()