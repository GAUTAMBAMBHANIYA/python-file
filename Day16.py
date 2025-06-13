# match case statements:
a=float(input("Enter your first Num:\n"))
b=float(input("Enter your second Num:\n"))
x=str(input("enter your calculator sign"))

match x:

     case '+':
         print("sum of given num is:",a+b)
     case '-':
        print("minius of given num is:",a-b)
     case '*':
        print("product of given num is:",a*b)
     case '/':
        print("divison of given num is:",a/b)
     case '**':
        print("power of given num is:",a**b)
     case '//':
        print("dd of given num is:",a//b)
     case _:
        print("invalid sign !!!!!!!!!!!")
         
    