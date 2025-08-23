
# Question 1
# Read two complex numbers and perform addition, subtraction, multiplication
a = complex(input())
b = complex(input())

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")

# Question 2
# Find the complex number with the largest magnitude from a list
numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
maxComplex = complex(0, 0)
maxAbs = 0

for i in numbers:
   if abs(i) > maxAbs:
       maxAbs = abs(i)
       maxComplex = i

print(maxComplex)
print(maxAbs)

# Question 3
# Read two complex numbers and an integer n, compute powers and sums with conjugates
n = int(input())
z1 = complex(input())
z2 = complex(input())

z_1 = z1.conjugate()
z_2 = z2.conjugate()

print(z1 ** n + z2 ** n + z_1 ** n + z_2 ** (n + 1))
