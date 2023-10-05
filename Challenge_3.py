class Student:
    def __init__(self):
        self.__name = None
        self.__rollNumber = None

    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name = name

    def get_rollNumber(self):
        return self.__rollNumber
    
    def set_rollNumber(self,rollNumber):
        self.__rollNumber = rollNumber

obj = Student()

obj.set_name("Sachin")
obj.set_rollNumber(4378848)

name = obj.get_name()
rollNumber = obj.get_rollNumber()
print(f"Name : {name} \nRoll Number : {rollNumber}")










# If i want user input values for name and roll Number and also need to iterate upto the number of user inputs the values:-

class Student:
    def __init__(self):
        self.__name = None
        self.__rollNumber = None

    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name = name

    def get_rollNumber(self):
        return self.__rollNumber
    
    def set_rollNumber(self,rollNumber):
        self.__rollNumber = rollNumber


student_list = []

while True:
    obj = Student()
    name = input(f"Enter The Name Of The Student Or (Press 00 To Quit) : ")
    if name == "00":
        break
    if name != "00":
        rollNumber = int(input(f"Enter The Roll Number Of The Student : "))
    
    obj.set_name(name)
    obj.set_rollNumber(rollNumber)
    student_list.append(obj)
    Name = obj.get_name()
    Roll_Number = obj.get_rollNumber()
    
    print(f"Name : {Name} \nRoll Number : {Roll_Number}")