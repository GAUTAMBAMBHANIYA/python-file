# custom error
# a=str(input("Enter the QUIT word"))
# if not a == "QUIT":
#     raise KeyError("you are wrong")


b=input("enter the num under 100 and greater then 0")
if (b<0 or b>100):
    raise ValueError("the num is not under 100 and greater then 0")     