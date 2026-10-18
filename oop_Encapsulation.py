# ENCAPSULATION:-
#       wrapping data and functions in a single unit(object)

#  ------ PRACTICE QUESTION ------
# create account class with 2 attributes balance, and acc_no, 
# create method for credit,debit, and printing the balance,

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def Debit(self, amount):
        self.balance -= amount
        print(f"RS. {amount} was debited")
        print(f"Total balance = {self.balance}")

    def Credit(self, amount):
        self.balance += amount
        print(f"RS. {amount} was credit")
        print(f"Total balance = {self.balance}")

    def get_balance(self):
        return self.balance

s1 = Account(10000, 1234)
s1.Debit(1500)
s1.Credit(1200)