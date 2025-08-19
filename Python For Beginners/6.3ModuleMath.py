
from math import *

# Question 1
# Calculates the distance between two points (x1, y1) and (x2, y2) using the distance formula
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)

# Question 2
# Computes the area and circumference of a circle given its radius R
R = float(input())
print(pi * R ** 2)
print(2 * pi * R)

# Question 3
# Calculates four types of means (arithmetic, geometric, harmonic, quadratic) of two numbers a and b
a = float(input())
b = float(input())

print((a + b) / 2)
print((a * b) ** 0.5)
print((2 * a * b) / (a + b))
print(((a ** 2 + b ** 2) / 2) ** 0.5)

# Question 4
# Evaluates sin, cos, and tan squared for an angle a given in degrees
a = float(input())
r = (a * pi) / 180
print(sin(r) + cos(r) + (tan(r) ** 2))

# Question 5
# Same as Question 4: evaluates sin, cos, and tan squared for an angle in degrees
a = float(input())
r = (a * pi) / 180
print(sin(r) + cos(r) + (tan(r) ** 2))

# Question 6
# Solves a quadratic equation ax^2 + bx + c = 0 and prints the roots
a = float(input())
b = float(input())
c = float(input())

D = (b ** 2) - (4 * a * c) 
if D > 0:
    x1 = (-b - sqrt(D)) / (2 * a)
    x2 = (-b + sqrt(D)) / (2 * a)
    if x1 < x2:
        print(x1)
        print(x2)
    else:
        print(x2)
        print(x1)
elif D == 0:
    print(-b / (2 * a))
else:
    print("No roots")

# Question 7
# Calculates the area of a regular n-sided polygon with side length a
n = float(input())
a = float(input())
print((n * (a ** 2)) / (4 * tan((pi / n))))