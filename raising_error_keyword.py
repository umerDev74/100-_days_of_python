
# --------  INSUFFIECENT BALANCE ERROR ------------

class InsuficentBalanceError(Exception):
    pass
balance = 5000
try:
    amount= int(input("Enter withdrawl Amount: "))
    if amount>balance:
        raise InsuficentBalanceError("Error: Insuficent Balance!")
    balance-= amount
    print("Withdrawl Successfully!")
    print(f"Remaining Balance = {balance}/")

except InsuficentBalanceError as e:
    print(e)
except ValueError:
    print("Please Enter Numbers only.")


# ************** INVALID MARKS ERROR ******************

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