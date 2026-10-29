class parentClass:
    def p_method(self):
        print("this is the parent method.1")

class childClass(parentClass):
    def p_method(self):
        print("umer 2")
        super().p_method()
    def c_method(self):
        print("this is the child method")
        super().p_method()

c_obj = childClass()
c_obj.c_method()
c_obj.p_method()

#      ------------ ANOTHER EXAMPLE ----------------

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class Programer(Employee):
    def __init__(self, name, id,lang):
        super().__init__(name, id)
        self.lang = lang

zohaib = Employee("zohaib khan","1234")
rohail = Programer("Rohail khan","5678","python")
print(rohail.name)
print(rohail.id)
print(rohail.lang)