num1=int(input("enter the number: "))
if(num1<0):
    print("Number is negative")
elif(num1>0):
    print("Number is positive")
    if(num1<=10):
        print("number is b/w 1-10")
    elif(num1>10 and num1<=20):
        print("number is b/w 11-20")
    else:
        print("the number is greter than 20")
else:
    print("Number is zero")