class InvalidMarksError(Exception):
    pass
try:
    marks = int(input("Enter the marks: "))
    if marks<0 or marks>100:
        raise InvalidMarksError("Error! Marks must be between 0 and 100")
    print("marks accepted")
except InvalidMarksError as e:
    print(e)
except ValueError:
    print("please enter marks only!")