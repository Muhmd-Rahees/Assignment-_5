class Account:
    def __init__(self,title=None,balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self,title=None,balance=0,interestRate=0):
        super().__init__(title,balance)
        self.interestRate = interestRate

Account1 = Account("Ashish",5000)
print(f"Account Title : {Account1.title}")
print(f"Account Balance : {Account1.balance}")

SavingsAccount1 = SavingsAccount("Ashish",5000,5)
print(f"Savings Account Title : {SavingsAccount1.title}")
print(f"Savings Account Balance : {SavingsAccount1.balance}")
print(f"Savings Account Interest : {SavingsAccount1.interestRate}")