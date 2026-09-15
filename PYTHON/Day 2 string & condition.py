                                        #STRINGS
#1 Concatination
str1 = "Jeevanshu"
str2 = " pal" 
print(str1 + str2)

str1 = "Jeevanshu"
str2 = " pal" 
finalstr = str1 + str2
print(str1 + str2)

# length of string
str1 = "Jeevanshu"
print(len(str1)) #9
str2 = " pal" 
finalstr = str1 + str2
print(str1 + str2)
print(len(finalstr)) #13

                                                            #Index [0,1,2,3,.............]
 #we can  only acces charcter not manuplate                                                            
str = "Jeevanshu"
print(str[0])

a = "hello"
ch = a[3]
print(ch)
                                                           #Slicing str[starting_idx : end_idx] ending idx not include
# access part of sting 
str = "Jeevanshu"
print(str[0:8]) #Jeevansh
print(str[:7]) #[0:7]
print(str[3:]) #[3:0]
#Negative Index [-5,-4,-3,-2,-1]
str = "Jeevanshu"
print(str[-10:-3]) #Jeevan
                                                          # STRING FUNCTION

str3  =  "i am learning python from zero"
print(str3.endswith("ero")) # give true
print(str3.endswith("zer")) # give false
print(str3.capitalize())
print(str3.replace("python","java"))
print(str3.find("f"))#21
print(str3.count("from")) #1
                                                              #Practice question
#Q1 - wap to input user first name & print its length
name = input("entr your first name ") 
print("lenght of your name is ",len(name))

#Q2 - wap to find a occurence in a string
dollar = "i $am $jeevan$hu i $tudy $tring"
print("occurnce of $ ",dollar.count("$")) #5

                                                               # condition statement
#if-elif-else
#if
age = 21
if(age>=18):
    print("you can vote")
  #elif   
light = "green"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("wait")
#else
light = "purple"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("wait")
else:
    print("light is broken")

                                                              # Practice 
# Give grade according to marks 
marks = int(input("enter your marks"))
if(marks>= 90):
    grade = "A"
elif(marks>= 80 and marks<=90 ):
    grade = "B"
elif(marks>=70 and marks<=80):
    grade = "c"
else:
    grade ="D"
print("grade of a student =",grade)

 #Q1 - wap to if number entered by user is odd or even 
num = int(input("enter a number"))
rem = num % 2
if(rem == 0):
    print("number is even")
else:
    print("number is odd") 
#Q2 - wap to find a greatest number
x = int(input("enter a first number"))
y = int(input("enter a second number"))
z = int(input("enter a third number"))
if(x > y and x > z):
    print("x is gratest ")
elif(y>z):
    print("y is greatest")
else:
    print("z is greatest")

#Q3 - wap to find number is multiple of 7 

q = int(input("enter a number "))
rem2 = q % 7
if(rem2 == 0):
    print("number is multiple of 7 ")
else:
    print("not multiple of 7")











