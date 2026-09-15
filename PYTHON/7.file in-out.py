                                                                  # File I/O
# python can be used  to perform operation in file ( read , write data)
# type of files :
#  text file --> .txt , .docx , .log etc .  
# binary file --> jpeg , mov , png ,mp4 , etc

# open ,read & close file 
f = open("notes.md","r") #( "file name or path" , "mode")
data = f.read()
print(data)
print(type(data))
f.close()

# write
f = open("notes.md","w")
f.write(" i am learning python") #overwrite
f.close
f = open("notes.md","a") # a = append
f.write(" from apna collage")
f.close
# with syntax
with open("notes.md","r") as f:
    data = f.read()
    print(data)
# # delteting file 
# import os
# os.remove( "file name")
                                                                   # practice
#Q1 create new file "practice.txt" using python add data                                                                   
with open("practice.txt","w") as f :
    f.write("hii everyone\nwe are learning file i/o from\napna collage/n")
    f.write("using python\ni like learning python")
 #Q2 replace all occurence of python into java
with open("practice.txt","r") as f:
    data = f.read()
new_data = data.replace("python","java")
print(new_data)
# check learning word is exist or not 
word = "learning "
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find( word) != -1) :
        print("found")
    else:
        print("not found")
# check first occurence of word  
def check_for_line():
    word = 'python'
    data = True
    line_no = 1
    with open("practice.txt", "r") as f :
        while data :
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1
check_for_line()


