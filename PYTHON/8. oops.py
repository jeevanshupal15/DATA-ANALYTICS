                                                                       # OOPs
# To map with real world scenarios, we can use the concept of Object-Oriented Programming (OOP) to model real-world entities and their interactions.
# OOP allows us to create classes that represent objects, encapsulate data, and define behaviors through methods. 
# This approach helps in organizing code, promoting reusability, and making it easier to maintain.
                                                         # Class & Object
# 1. class : class is a blueprint or template for creating objects. 
class Student:  # class
    name = "Jeevanshu pal"
    course = "bca"
s1 = Student()  # object
print(s1.name)  # accessing attribute of object
print(s1.name)  # accessing attribute of object
print(s1.course)

# init function :  special method in Python classes that is automatically called when an object of the class is created.    
class Student:
    collage_name = "IAMR"  # class attribute
    def __init__(self):  #default constructor
        pass
    def __init__(self , name, age): #parametrized constructor
        self.name = name #self.name = object attribute > class attribute , both have same value
        self.age = age
    def welcome(self): # method
        print("Welcome student ",self.name,self.age)
 # static method : dont use self parameter (work at class level)
    @staticmethod #decoretor
    def hello(): # method
        print("Welcome student in static method")    
s1 = Student("pavitra",17,) 
print(s1.name,s1.age,s1.collage_name)    
s2 = Student("abhinav",19)     
print(s2.name,s2.age,s2.collage_name)  
s1.welcome() 
s2.welcome() 
s1.hello() 

                                                                   # Abstraction
 # hiding the internal implementation details and showing only the necessary features to user.
class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc = True
    print("car is started")
car1 = car()
car1.start()
                                                                      #encapsulation 
# wrapping up of data and methods into a single unit called class. 

# delete keyword
class truck:
    def __init__(self,name):
        self.name = name
t1 = truck("tata")
print(t1.name)
del t1.name
#print(t1.name)  # This will raise an AttributeError

#public & private attibute method 
class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no  # public attribute
        self.__acc_pass = acc_pass  # private attribute using double underscore 
    def reset_pass(self):
        print(self.__acc_pass)
acc1 = account(123456,"abc@123")
print(acc1.acc_no)  # accessing public attribute
#print(acc1.__acc_pass)  # This will raise an AttributeError
print(acc1.reset_pass())  # accessing private attribute through method

#inheritance : mechanism in which one class can inherit the properties and methods of another class.
# single level inheritance
class car:
    color = "black"
    @staticmethod
    def start():
        print("car is started")
    def stop(self):
        print("car is stopped")
class toyota(car):  # child class
    def __init__(self,name):
        self.name = name
car1 = toyota("fortuner" )
car2 = toyota("innova")
print(car1.name,car1.color)
print(car2.name,car2.start())
#multilevel inheritance
class car:
    color = "black"
    @staticmethod
    def start():
        print("car is started")
    def stop(self):
        print("car is stopped")
class toyota(car):  # child class
    def __init__(self,brand):
        self.brand = brand
class fortuner(toyota):  # grandchild class
    def __init__(self,type):
        self.type = type
car1 = fortuner("diesel")
print(car1.start())
#multiple inheritance
class A:
    valA = "welcome to class A"
class B:
    valB = "welcome to class B"
class C(A,B):  # child class inheriting from both A and B
    valC = "welcome to class C"

c1 = C()
print(c1.valA)
print(c1.valB)
print(c1.valC)
# class method : method that is bound to the class and not the object of the class. It takes cls as first parameter instead of self.
class person:
    name = "anynymous"
    def __init__(self,name): #method 1
        self.__class__.name = name
    @classmethod
    def change_name(cls,name): #method 2
        cls.name = name
p1 = person("rahul")
p1.change_name("jeevanshu")
print(p1.name)
print(person.name)
#property decorator
class Student:
    def __init__(self,phy,chem,maths):
        self.pht =phy
        self.chem  = chem
        self.maths = maths
    @property
    def avg(self):
        return (self.pht + self.chem + self.maths) / 3
stu1 = Student(45,88,78)
print(stu1.avg)
stu1.chem = 33
print(stu1.avg)

# polymorphism : operator overloading and method overloading
class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def shownumber(self):
        print(self.real,"i+",self.img,"j")
    def __add__(self,num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img    
        return complex(newreal,newimg)

    def __sub__(self,num2):
        newreal = self.real - num2.real
        newimg = self.img - num2.img
        return complex(newreal,newimg)
num1 = complex(2,3)
num1.shownumber()
num2 = complex(4,5)
num2.shownumber()
num3 = num1 + num2
num3.shownumber()
num4 = num1 - num2
num4.shownumber()

                                                                        # practice
# Q1 lets practice classs that takes name and marks of  3 subject as argument in constructor. then create a method to calculate average marks.
class Student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
    def get_avg(self):
        sum = 0
        for val in self.mark:
            sum += val
        print("hii",self.name,"your avg score is ",sum/3)
s1 = Student("hulk",[45,88,78])
s1.get_avg()
# Q2 create a account class with 2 attributes name and account no. create a method to debit and credit money from account. 
# also create a method to display balance.
class accounts:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account = acc
    def debit(self, amount):
        self.balance -= amount
        print("your amount is debited",amount)
        print("your account balance is ",self.balance)
    def credit(self, amount):
        self.balance += amount
        print("your amount is credited",amount)
        print("your account balance is ",self.balance)
    def display_balance(self):
        return self.balance

acc1 = accounts(100000,123456)
acc1.debit(5000)
acc1.credit(10000)
acc1.display_balance()
acc1.debit(50000)

#Q3 define a class to create a circle with radius as an attribute. create a method to calculate area and circumference of circle. 
# and area and circumference should be displayed when object is printed.
class  circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius **2
    def circumference(self):
        return 2 * 3.14 * self.radius
c1 = circle(5)
print("area of circle is ",c1.area())
print("circumference of circle is ",c1.circumference())

#Q4 define a employee class with attributes role, department, salary. create a method to display employee details 
# and also create  engineer class that inherits employee class and has additional attribute name , age 
class employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary
    def display_details(self):
        print("Role:",self.role)
        print("Department:",self.department)
        print("Salary:",self.salary)


class engineer(employee):
    def __init__(self,name,age):
        super().__init__("Engineer", "Engineering", 50000)
        self.name = name
        self.age = age
    def display_engineer_details(self):
        self.display_details()
        print("Name:",self.name)
        print("Age:",self.age)
e1 = employee("Manager", "Management", 70000)
e1.display_details()
e2 = engineer("Alice", 30)
e2.display_engineer_details()
