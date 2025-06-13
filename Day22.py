# list
"""Lists are ordered collection of data items.
   They store multiple items in a single variable.
   List items are separated by commas and enclosed within square brackets [].
   Lists are changeable meaning we can alter them after creation."""

lst1=[1,2,3,4,5,6,7,8]
print(lst1)
print(type(lst1))

lst2=["apple","mango","orange"]
print(lst2)

# List Index
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]  positive indexing
#          [-5]    [-4]    [-3]     [-2]      [-1] nagative indexing

if 3 in lst1:
    print("yes")
else:
    print("no")

# Range of Index:
# You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range.

# Syntax:

# listName[start : end : jumpIndex]
print(lst1[:])
print(lst1[1:6])
print(lst1[0:7:2])

# Example: printing elements within a particular range:
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'

# List Comprehension
# List comprehensions are used for creating new lists from other 
# iterables like lists,tuples, dictionaries, sets, and even in arrays and strings.
lst3=[i+1 for i in lst1]
print(lst3)
   
lst4=[i*i for i in lst1 if i%2==0]
print(lst4)