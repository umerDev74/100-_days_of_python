#  create student class that takes names and marks of 3 subjects and arguments in constructor 
#        then create a method to print the average ? >>>>>

class student:
    #      this is a constructor method
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    #     now average function 
    def get_avg (self):
        sum = 0
        for value in self.marks:
            sum += value

        print(f"Hi {self.name} your average score is: ",sum/3)

s1 = student("umer", [89,97,83])
s1.get_avg()

# ------- STATIC METHOD ---------------

class hello():
    @staticmethod
    def hi():
      print("Hello World")
s1=hello()
s1.hi( )