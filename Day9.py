#typecasting
# 1. Implicit Typecasting
# Done automatically by Python.
# Happens when Python promotes a variable to a more complex data type to avoid data loss.


a = 5        # int
b = 2.0      # float
c = a + b    # int + float = float
print(c)     # Output: 7.0
print(type(c))  # <class 'float'>

# 2. Explicit Typecasting
# Done manually by the programmer using functions like int(), float(), str(), etc.

# float to int
a = int(3.7)       # Output: 3

# string to int
b = int("10")      # Output: 10

# int to string
c = str(25)        # Output: '25'
