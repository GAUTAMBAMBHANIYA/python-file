#  loop with else statement
for i in range(6):
    print(i+1,end="**")
else:
    print("there is not i")

for i in range(1,50,2):
    print(i)
    if i==9:
     break
else: #else process after complete loop but not after break
    print("there is not i")