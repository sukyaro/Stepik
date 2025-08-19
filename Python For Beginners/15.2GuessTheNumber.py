
from math import log2

# Question 1
# This code calculates the minimum number of bits needed to represent the input number in binary.
n = int(input()) 
a = log2(n)
if a - int(a) != 0:
    print(int(a) + 1)
else:
    print(int(a))
