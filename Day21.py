# Function arguments

def defaultargs(a,b=2):
    print("avg of two numbers",(a+b)/2)


def numbersargs(a,b):
    print("avg of two numbers",(a+b)/2)


def arbitaryargs(*args):
    sum=0
    for i in args:
        sum+=i
    print("avg of",len(args),"nUMbers are",sum/len(args))


def keywordargs(fname,mname,lname):
    print(fname,mname,lname)
while True:
 print("================Function arguments===============")
 print(" 0 for stop args")
 print(" 1 for the default argument:")
 print(" 2 for the numbers argument:")
 print(" 3 for the arbitary arguments,*args:")
 print(" 4 for the keyword arguments:")

 x=int(input("Enter the chice for the argument:"))
 match x:
    case 0:
         print("stop the arguments")
         break
    case 1:
        defaultargs(2)
        defaultargs(2,35) # avg of 2,35

    case 2:
        numbersargs(5,3)
    
    case 3:
        arbitaryargs(4,5,6)
    case 4:
        keywordargs(lname="Bambhaniya",fname="Mr.",mname="Gautam")
    case _:
        print("invalid function args!")