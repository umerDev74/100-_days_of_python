class Employee:
    Company = "Apple"

    def Show(self):
        print(f"The name is {self.name} and company is {self.Company}")

    @classmethod
    def Changename(cls, newcomp):
        cls.Company = newcomp

e1 = Employee()
e1.name = "Umer"
e1.Show()

e1.Changename("Tesla")
e1.Show()
print(Employee.Company)