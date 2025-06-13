#list methods

#sort()
l=[1,4,3,2,1,5,3,2,1,9]
l.sort()
print(l)

# desinding order
l.sort(reverse=True)
print(l)

#reverse()
colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)

# index()
# This method returns the index of the first occurrence of the list item.
m=l.index(9)
print(m)

#count()
print(l.count(1))

#copy()
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)

# append():
# This method appends items to the end of the existing list.
l.append(45)
print(l)

# insert():
# This method inserts an item at the given index.
#  User has to specify index and the item to be inserted within the insert() method.

l.insert(2,90)
print(l)

#extends()
#This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
l.extend(colors)
print(l)

