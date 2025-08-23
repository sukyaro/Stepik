
from random import *

# Question 1
# Estimate the area of a region defined by inequalities using Monte Carlo method
n = 10**6
k = 0
S0 = 16

for _ in range(n):
   x = uniform(-2, 2)
   y = uniform(-2, 2)

   if (x ** 3 + y ** 4 + 2 >= 0) and (3 * x + y ** 2 <= 2):
       k += 1

print((k/n) * S0)

# Question 2
# Estimate the area of a unit circle using Monte Carlo method
n = 10 ** 6
k = 0
S0 = 4

for _ in range(n):
    x = uniform(-1, 1)
    y = uniform(-1, 1)

    if (x ** 2 + y ** 2) < 1:
        k += 1

print((k/n) * S0)
