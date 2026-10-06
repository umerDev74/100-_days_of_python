#     USE OF CLASS AND OBJECT >>>>>>>>>>>

class person:
    name = "umer"
    occupation = "AI Engineeiar"
    networt = 50000

obj1 = person()
print(obj1.name,obj1.occupation,obj1.networt)

#      USE OF FUNCTION AND SELF PARAMETER IN CLASS AND OBJECT >>>>>>>>>>

class person:
    name = "umer"
    occupation = "AI Engineeiar"
    networt = 50000
    def info(self): # SELF ka matlb wo object jis ke liye ye method call kiya jata hai
        print(f"{self.name} is an {self.occupation} and his networth is {self.networt}")

a = person()
b = person()
b.name = "Zohaib"
b.occupation = "HR"
b.networt = 100000
a.info()
b.info()