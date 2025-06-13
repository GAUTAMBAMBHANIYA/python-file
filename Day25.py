# tuple method
# Tuples are immutable, hence
#  if you want to add, remove or change tuple items, 
# then first you must convert the tuple to a list.
#  Then perform operation on that list and convert it back to tuple.

tup1=(1,4,3,5,3,2)
l1=list(tup1)
l1.append(99) #add
l1.pop(3)     #remove
l1[0]=50
tup2=tuple(l1)
print(tup2)

# concating two tuple
tup3=(1,2,4,8,)
tup4=("harry","gautam","me")
tup5=tup3+tup4
print(tup5)

# count
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)

# index()
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is', res)