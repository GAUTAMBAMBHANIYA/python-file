#import works
import math
print(math.log(1))

# You can also import specific functions or variables from a module using the from keyword.
from math import sqrt
result=sqrt(100)
print(result)

# using * you can import all function from the math
from math import *
print(max(2,9))
print(min(2,9))
print(cosh(1))

# The "as" keyword 
# import math as m

# using dir function you can print all the function from math

import pandas
print(dir(pandas))