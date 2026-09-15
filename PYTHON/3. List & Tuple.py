                                                             # List 
# A built in data type stores a set of a value [ integer,float,string,etc]. It is mutable 
marks1 =  50
marks2 =  60
marks3 =  70
marks4 =  80
marks = [50,60,70,80] # this is a list
print(len(marks))
print(marks[2])

student = ["jeevanshu",19,"bca"]
print(student[0])
student[0] = "pal" #mutable 
print(type(student))                                                          # List Slicing [strt_idx:end_idx]
num =  [10,20,30,40,50,60,70,80,90,100]
print(num[2:7])  
print(num[:7])
print(num[2:])   
print(num[-7:-2])                                                           
                                                                 # List Method 
list =  [10,80,70,40,50,50,30,60,20,60,90,100]
list.append(110) # add element in list
print(list) 
list.sort() # sort in ascending
print(list) 
list.sort(reverse=True) # sort in descending
print(list) 
list.reverse() # Reverse in List
print(list) 
list.insert(4,200) # insert element at index
print(list) 
list.remove(50) # remove first occurence of element
print(list) 
list.pop(7) # remove element at index
print(list) 
                                                                 #Tuple (1,2,3,45,)
# This is immutable
tup = (10,80,70,40,50,50,30,60,20,60,90,100)
print(type(tup))
print(tup)
print(tup[3:7])
#tuple method
print(tup.index(50)) # 4  , return index of first occurence
print(tup.count(50))  #2  , count total occurence
                                                                    # Practice Question
#Q1 - wap to ask the user to enter their fav movie name & store in a lsit
movie = []
mov1 = input("enter your 1 fav movie name =")     
mov2 = input("enter your 2 fav movie name =")  
mov3 = input("enter your 3 fav movie name =")    
movie.append(mov1) 
movie.append(mov2) 
movie.append(mov3) 
print(movie)

#Q2 - wap to check number is palindrome or not
palli = [1,3,3,1]
copy_palli = palli.copy()
copy_palli.reverse()
if(palli == copy_palli):
    print("num is pallindrome")
else:
    print("not")

palli = [1,2,3,1]
copy_palli = palli.copy()
copy_palli.reverse()
if(palli == copy_palli):
    print("num is pallindrome")
else:
    print("not")


                                                         