#functions 

def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    return fact

n=int(input("enter your n numbers:"))
r=int(input("enter your r numbers:"))

Ncr =factorial(n)/ (factorial(r) *factorial(n-r))
print("your ncr is as below:",Ncr)


