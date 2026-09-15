                                                                  #Dictonary { "key" : "value"       }
# dictonary are used to store data and value in {key : pair} , it is mutable 
# dont allow duplicate key
info = {
    "key": "vlaue",
    "name" : "jeevansshu",
    "age": "19",
    "marks" : 88.79
}
print(info)
print(type(info))

# add new element in dic
info["name"] = "pavitra"
info["course"] = "bca"
print(info)

#nested dictonary
student = {
    "name" : "Jeevansu pal",
    "subject" : {
        "phy" : 91,
        "chem" : 78,
        "math" : 58,

    }

}
print(student)
print(student["subject"])
print(student["subject"]["math"])
  #Dictonary Method

student = {
    "name" : "Jeevansu pal",
    "subject" : {
        "phy" : 91,
        "chem" : 78,
        "math" : 58,

    }

}
print(student.keys())        
print(list(student.keys())) #typecast in list  
print(student.values()) 
print(list(student.values())) # conver in list
print(student.items()) #return all pair as tuple
print(list(student.items()))
print(student.get("name")) #return the key according to value
print(student.update({"city":"ghaziabad"})) # insert specific item in dic
print(student) 
                                                                         #Sets {1,2,3,4,5,6,7,}
#repated element store only once  , set is mutable but element is immutable 
collection = {1,2,3,4,4,5,6, "hello"}     
print(set)
print(type(set))
null ={} #this is not set it is a dictonary
coll= set() #this is empty set
print(type(coll))
#set method
coll= set() #this is empty set
coll.add(1)# add element
coll.add(2)
coll.add(3)
coll.add("learn pyton")
coll.add("jeevnashu")
coll.add((1,2,3,4,5))
print(coll)
coll.pop() #remove random value
print(coll)
colll = {1,9,8,7,6,5,4,}
colll.clear() #empty the value
print(colll)
set1 = { 1,4,6,7,4,}
set2 = {1,4,5,7}
print(set1.union(set2)) # combine both set
print(set1.intersection(set2)) # commen element

                                                                      
                                                                       