class Person:
    __name = "umer"

    def __Hello(self):
        print("Hello Person!")

    def welcom(self):
        self.__Hello()

p1 = Person()
p1.welcom()

# -------------------------------

class BankAccount:
    def __init__(self, name, balance):
        self.name = name   # public attribute
        self._branch_code = "XYZ123"  # Protected attribute
        self.__balance = balance  # Private attribute

    def check_balance(self,pin):
        if pin == "1234":
            return self.__balance
        else:
            return "Access Denied"


b1 = BankAccount("John Doe", 1000)
print(b1.name)  # Accessing public attribute
print(b1._branch_code)  # Accessing protected attribute (not recommended)
print(b1.check_balance("1234"))  # Accessing private attribute through method