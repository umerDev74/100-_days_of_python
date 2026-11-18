# Parent Class (General Blueprint)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner}: ${amount} nikal liye. Baqi balance: ${self.balance}")
        else:
            print(f"{self.owner}: Balance kam hai!")


# Child Class 1: Savings Account (Specific Limits)
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance):
        super().__init__(owner, balance)
        self.withdraw_count = 0  # kitni baar paise nikale gaye

    # Overriding withdraw method
    def withdraw(self, amount):
        if self.withdraw_count >= 3:
            print(f"{self.owner}: Limit poori ho chuki hai! Is mahine mazeed paise nahi nikal sakte.")
        else:
            self.withdraw_count += 1
            # Parent class wale withdraw logic ko call kar rahe hain
            super().withdraw(amount)


# Child Class 2: Current Account (Overdraft facility)
class CurrentAccount(BankAccount):
    def __init__(self, owner, balance, overdraft_limit=500):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit  # extra nikalne ki limit

    # Overriding withdraw method
    def withdraw(self, amount):
        # Yahan balance 0 hone par bhi overdraft check hoga
        if amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"{self.owner} (Current Account): ${amount} nikal liye. Naya Balance: ${self.balance}")
        else:
            print(f"{self.owner}: Overdraft limit se bhi zyada amount hai! Transaction Rejected.")


# --- Test karte hain ---

print("--- Savings Account Test ---")
user1 = SavingsAccount("Ali", 1000)
user1.withdraw(100) # 1st time
user1.withdraw(100) # 2nd time
user1.withdraw(100) # 3rd time
user1.withdraw(100) # 4th time -> Limit Error aayega!

print("\n--- Current Account Test ---")
user2 = CurrentAccount("Usman", 200, overdraft_limit=500)
# Balance sirf 200 hai lekin hum 500 nikal rahe hain (Overdraft ki wajah se allow hoga)
user2.withdraw(500)