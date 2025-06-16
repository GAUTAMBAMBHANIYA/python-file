
import random
import string

def add_random_letters(s):
    before = ''.join(random.choices(string.ascii_lowercase, k=3))
    after = ''.join(random.choices(string.ascii_lowercase, k=3))
    return before + s + after
def coding():
  words = str1.split()
  result = ""
  for i in words:
    if result != "":
        result = result + " "
    if len(i) <= 2:
    
        result = result + i[::-1]
    else:
        # Move the first letter to the end
        s = i[1:] + i[0]
        result = result + add_random_letters(s)
  print("Final output in one line:", result)

def decod():
 decoding=str1.split()
 result= ""
 for i in decoding:
      if result != "":
        result = result + " "
      if(len(i)<=2 and len(i)>=9):
       if len(i) <= 2:
    
        result = result + i[::-1]
       else :
        decodeword1=i[3:-3]
        newword=decodeword1[-1]+decodeword1[:-1]
        result+=newword
      else:
        print("invalid decode please enter the proper code")
        break
     
 print(result)
while True:
 str1 =input("Enter the code\n")
 print("..................Secrate code language....................")
 print("1 . For the code language ")
 print ("2 . For the decode language")
 try:
  choice=int(input("Enter the input 1 for the coding:"))
 except:
  raise ValueError("number is not valid ")

 if choice==1:
   coding() 
 else: 
   decod()

# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode



