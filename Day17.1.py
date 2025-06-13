#range(start,end,step)
# start	Optional. An integer number specifying at which position to start. Default is 0
# stop	Required. An integer number specifying at which position to stop (not included).
# step	Optional. An integer number specifying the incrementation. Default is 1

for i in range(6):
   print(i) #print 0 to 5
#  print(i+1) #print 1 to 6

for i in range(2,10):
   print(i) # print 2 to 9

for i in range (1,100,2):
   print(i) # print 1,3,5,7.......................91,93,95,97,99 

#if range(0,100,5) so print  5,10,5.......