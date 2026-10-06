def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning!")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello World!")

@greet
def add(a,b):
    print(a+b)

add(1,2)
hello()
