class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
    
    def interestAmount(self):
        self.interestAmount = (self.interestRate * self.balance) / 100
        return self.interestAmount



demo1 = SavingsAccount("Ashish", 2000, 5)   
demo1.deposit(500)
demo1.getBalance()
print(f"The Balance After Depositing 500 : {demo1.getBalance()}")

demo1.withdrawal(500)
demo1.getBalance()
print(f"The Balance After 500 withdrawn : {demo1.getBalance()}")

demo1.interestAmount()
print(f"The Interest Amount is : {demo1.interestAmount}")

