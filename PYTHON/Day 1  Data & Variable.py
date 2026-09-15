                                       #Variable
  #name is a variable , jeevanshu pal is value of a varible , value assigne left to right 
  # keyword is reserved words in python
    
name ="Jeevansu pal"  
age = 19 
course = "BCA"
collage = "IAMR"

print("enter your name : ",name )
print("enter your age :",age)
print("name of your course :",course)
print("enter our collage name :",collage)

                              #Data Type
    #integer = 1,25 ,45, string = hello, hii , delhi, float = 12.23,99.99, boolean = true or false  , none 

name ="Jeevansu pal"  
age = 19 
percentage= 78.78
collage = True

print(type(name ))   #string
print(type(age))     #integer
print(type(percentage)) #float
print(type(collage))    # boolean

                                                          # PRINT SUM

a = 10
b = 30
sum = a + b
print(sum)

                                          # operators

#arithmatic operators ( +,-,%,*,/,**)
a = 20
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #remainder
print(a**b) #power

# comparison operator (==,!=,<,>,=<,>=) it give always boolean value

a = 50
b = 20
print(a==b) #false
print(a!=b) #true
print(a>b)  #true
print(a<b)  #false
print(a>=b) #true
print(a<=b) #false

#assignment operator (+=,-=,%=,*=,/=,**=)
num = 10
num += 10
print("num",num) #20
# logical operator (not , and , or ) boolean expression

a = 50
b = 30
print(not False) #true
print(not(a>b)) #false

val1 = True
val2 = True
print("and operator",val1 and val2) #true

val1 = True
val2 = False
print("and operator",val1 and val2) #false
print("or operator",val1 or val2) #true

val1 = True
val2 = True
print("and operator",val1 and val2) #true
print("or operator",val1 or val2) #true

val1 = False
val2 = False
print("or operator",val1 or val2) #false

                                                           # TYPE CONVERSION
#1. conversion = automatically    
a = 2
b = 4.25
sum = a + b  #2.00 + 4.25
print(sum)          

# casting = manually

a = int("2")
b = 4.25
sum = a + b  #2.00 + 4.25
print(type(a)) #int
print(sum) 

x = str("3.14")
print(type(x)) #string


                                                          # INPUT IN PYTHON 
   # it convert integer , float into string always                                                         
name1 = input("enter your name :")
print("welcome",name1)

val = input("enter your value : ")
print(type(val),val)

int("5")
val3 = int(input("enter your value : "))
print(type(val3),val3) #int

                                                    # PRACTICE QUESTION
  #Q1  WAP to input two number and print their sum

first = int(input("enter your first num :"))
second = int(input("enter your second num :"))    
print("sum = " ,first + second)

#Q1  WAP to input side of a square and print area

side = int(input("enter side : "))
print("area=",side**2)


         