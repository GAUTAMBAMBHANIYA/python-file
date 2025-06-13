# string slicing
str1="gautam"

# using len() function we can find len of String

print(len(str1))
print(str1[0:6]) # including 0 but not 6 
print(str1[:6])  # as above
print(str1[0:])  # print 0 to lenth
print(str1[1:-3]) # print 1 to len(str1)-3 ==> [1:3]
print(str1[-5:-1]) # print 1 to 5 => [1:5]