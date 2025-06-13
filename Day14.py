# if else
age=int(input("enter your age\n"))
if(age<18):
    print("you can't vote:")
else:
    print("you can vote:")


# el if
num=int(input("enter the number"))
if(num>0):
    print("positive")
elif(num==0):
    print("zero")
else:
    print("negetive")
    

# nested if else
a=int(input("enter your age\n"))
if(a<18):
    print("you are in limited age")
else:
    if (a>=18 and a<21):
         print("you can't elect for the m.l.a.")
    else:
        print("you can elct for the m.l.a.")