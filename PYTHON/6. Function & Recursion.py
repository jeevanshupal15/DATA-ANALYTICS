                                                                 #Function
#deifine function
def calc_sum(a,b) :
    return a+b
sum = calc_sum(1,3) # 4 output
print(sum)
# average of 3 number 
def calc_avg(a,b,c):
    sum =a+b+c
    avg = sum/3
    print(avg)
    return avg
calc_avg(3,5,7)

def calc_prod(a=2,b=4): # defalt parameter
     print(a*b)
     return a*b
calc_prod() 


                                              #practice 
#Q1 wap to pint length of a list( lsit is parameter):
cities = ["delhi","mumbai","pune","jaipur","gzb"]
heroes = ["iron","thor","loky","goku"]
def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)
#Q2 wap to print element of list in single line ( list is the parameter)
cities = ["delhi","mumbai","pune","jaipur","gzb"]
heroes = ["iron","thor","loky","goku"]
def print_list(list):
    for item in list:
        print(item, end="  ")

print_list(cities)
print_list(heroes)
# Q3 wap to find a factorial of n ( n in parameter)
def calc_fact(n):
     fact = 1
     for i in range(1,n+1):
         fact *= i 
     print(fact)
calc_fact(7)
# Q4 wap to convert usd in inr 
def converter(usd_value):
    inr_value = usd_value * 94 
    print(usd_value,"USD=",inr_value,"INR")
converter(45)

# Q5 wap to check number is odd or even 
def checker(n):
    if(n%2 == 0):
        print("even")
    else:
        print("odd")
checker(3)
                                                                  #Recursion ( function calls it slf repeatdly )  
#recursive function
def show(n):
    if(n == 0):# base case or stop condition
        return
    print(n)
    show(n-1)
show(10)  

# Recursion  ((reccurence relation)
def fact(n):
    if(n == 1 or n == 1) :
        return 1
    else:
        return fact(n-1)*n  
print(fact(4))     

                                                               # practice question
def calc_add(n):
    if(n==0):
        return 0
    return calc_add(n-1) + n
sum =calc_add(4)  
print(sum)                                                             