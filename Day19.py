# break and continue statement


#break()
# With the break statement we can stop the loop even if the while or for condition is true:

for i in range(5):
    if(i==4):
     break
    print(i)

#contine()
# With the continue statement we can stop the current iteration, and continue with the next:
i=0
while(i<10):
   i+=1
   if(i==5):
    continue
    print("this literal is stop by continue statement ")
   print(i)
  