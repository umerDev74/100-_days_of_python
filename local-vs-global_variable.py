x=10 #global variable

def my_function():
    global x
    x=20 #modifying global variable

    y=5
    print(y) #local variable

my_function()

print(x)