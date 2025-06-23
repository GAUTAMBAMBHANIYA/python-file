# file  handling

# opening a file
f=open('myfile.txt','r')
text=f.read()
print(text)
f.close()

#writing the file
m=open('myfile2.txt','w')
m.write("hey jarvis how are you!")

# append the file
m=open('myfile2.txt','a')
m.write("hey jarvis how are you!")
m.close()

# Alternatively, you can use the with statement to automatically close the file after you are done with it.

with open('myfile.txt','a')as f:
    f.write("this is a beaytiful view")
    
