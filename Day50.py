# read(),readline()
# The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.

f=open('myfile.txt','r')

i=0
while True:
 line=f.readline()

 if not line:
   break
 i=i+1
 m1=line.split(",")[0]
 m2=line.split(",")[1]
 m3=line.split(",")[2]

 print(f"Mark of student {i} in maths is:{m1}")
 print(f"Mark of student {i} in maths is:{m2}")
 print(f"Mark of student {i} in maths is:{m3}")
 print(line)



#writeline()
# The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.
f1=open('myfile3.txt','w')
lines=("line 1\n","line 2\n")
f1.writelines(lines)
f.close()
