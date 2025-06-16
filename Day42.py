#Enumerate function

marks=[98,76,8,6,8,65,44,22,3,2,100]

for index,mark in enumerate(marks):
    print(mark)
    if index==0:
        print("you are awsome!")

for index,mark in enumerate(marks,start=1):
    print("{",index,mark,"}",end=" ")
   
