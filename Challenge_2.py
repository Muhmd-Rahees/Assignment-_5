# In this exercise, you have to implement a calculator that can perform addition, subtraction, multiplication, and division

class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def division(self):
        return self.num1 / self.num2

obj = Calculator(94,10)    
res_add = obj.add()
res_subtract = obj.subtract()
res_multiply = obj.multiply()
res_division = obj.division()

print(f"Addition : {res_add}\nSubtraction : {res_subtract}\nMultiplication : {res_multiply}\nDivision : {res_division}")


