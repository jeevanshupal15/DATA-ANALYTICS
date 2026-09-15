                                                                       # Loops
#while loops
count = 1
while count <= 5:
    count += 1
    print("hello") 

i = 1
while i <= 50:
    i += 1
    print("hello",i) 
                                                                       #Practice
# Q1 wap to print number from 1 to 100.
a = 0
while a < 100 :
    a += 1
    print(a)
# Q2 wap to print number from 100 to 1.
a = 100
while a >= 1:
    a -= 1
    print(a)
# Q3 wap to print a multiplication of an number
a = 0
n =int(input("enter your number "))
while a < 10:
    a += 1
    print(n*a)
# Q4 print the elemnt of the following list [1,4,9,16,,25,36,47,64,81,100]
list = [1,4,9,16,25,36,47,64,81,100]
id = 0
while id < len(list):
    print(list[id])
    id += 1
# Q5 search the  x elemnt in the following tuple (1,4,9,16,,25,36,47,64,81,100)

tuple = (1,4,9,16,25,36,47,64,81,100)
x = 36
idx = 0 # initialization
while idx < len(tuple):
    if(tuple[idx] == x):
        print("found at idx",idx)
    idx += 1

# Break and continue
# break  : used to terminate the loop
a = 1
while a <= 10:
    print(a)
    if(a == 3):
     break
    a += 1
print(" end of loop")
#Continue : used to terminate the current iteration & continue the execution
a = 0
while a <= 10:
    if(a == 3):
     a += 1
     continue  #skip
    print(a)
    a += 1
# For loop
list = [1,4,9,16,25,36,47,64,81,100]
for val in list :
    print(val)
#for loop with else
ist = [1,4,9,16,25,36,47,64,81,100]
for val in list :
    print(val)
else:
    print("end of code")
#range( return sequence of number starting from zerp by default and incriment by one and stop before speciied number )
#range(start,stop,step)
for i in range(10): # stop condition
    print(i)
for i in range(2,10): # start,stop
    print(i)
for i in range(2,10,2): # start,stop,step
    print(i)
# Pass 
for i in range(10): # stop condition
    pass
print("null")

                                                                          # Practice

# Q1 print the elemnt of the following list using for loop [1,4,9,16,,25,36,47,64,81,100]
list = [1,4,9,16,25,36,47,64,81,100]
for el in list :
    print(el)
# Q2 search the  x elemnt in the following tuple using for loop (1,4,9,16,,25,36,47,64,81,100)
tuplee = (1,4,9,16,25,36,49,64,81,100)
y = 49
idxx = 0
for ell in tuplee:
    if(ell==y):
        print("number found at idx ",idxx)
    idxx += 1

# Q3 print table using range 
n = int(input("enter num :"))
for i in range(1,11):
    print(i*n)
#Q4 wap to sum of first n number using while loop
n = 7
sum = 0
i=1
while i <= n:
    sum += i
    i += 1
print("total sum = ",sum)

