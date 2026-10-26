class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, string):
        return cls(string.split("-")[0], int(string.split("-")[1]))

e1 = Employee("Umer", 50000)
print(e1.name)
print(e1.salary)

e2 = Employee.from_string("Ali-60000")
print(e2.name)
print(e2.salary)