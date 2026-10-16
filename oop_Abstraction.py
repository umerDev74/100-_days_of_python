# ABSTRACTION:-
#               hiding the implementation detail of a class and only showing the
#               essential features to the user >>>>>>>>
#         EXAMPLE PROGRAM

class car():
    def __init__(self):
         self.accelator = False
         self.brk = False
         self.clutch = False

    def start(self):
         self.clutch = True
         self.accelator = True

         print("Car started ....")

car1 = car()
car1.start()

#  in the above example we have seen that the implementatio detail of a car is hide
#  in class and funstions and the the information of objects are unhide 
# thats called the abstarction 