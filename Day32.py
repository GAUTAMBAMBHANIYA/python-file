# set mehod
 
s1={12,5,6,7}
s2={12,5,9,8,6,}

#1.Union & update()
print(s1.union(s2))
s1.update(s2)
print(s1,s2)

#2.intersection & intersection_update
s1={"jamu","kashmir","gujrat","diu"}
s2={"jamu","kashmir","punjab"}
print(s1.intersection(s2))
print(s1.intersection(s2))

#3 symmetric_diffrence
print(s1.symmetric_difference(s2))

#diffrence & dif update()
print(s1.difference(s2))
print(s1.difference_update(s2))

#disjoint
# a and b = 0
set1={12,5,6,7,9,8}
set2={12,5,9,8,6,}
print(set1.isdisjoint(set2))

#issuperset() value of all set 2 is present in set 1
print(set1.issuperset(set2))
print(set2.issubset(set1))

#remove and discard 
g={"gautam","my","name","is","jamnagar"}
print(g.remove("jamnagar"))
g.discard("jamsndsuidf") # don't throw a error

#pop
item=g.pop()
print(g)
print(item)

#del and clear
h={80,2,2,32,44,2,1,1,3,1,3,4,}
# del h delete this set
print(h.clear)
 
