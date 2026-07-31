a= int(input("Enter the number between 4 and 8: "))
if(a<4 or a>8):
    raise ValueError("the number should be between in 4 and 8!")
else:
    print("the number is correct")