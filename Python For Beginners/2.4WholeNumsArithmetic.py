
# Part 1

# Question 1
# Reads a number and prints it, the next number, and the one after
a = int(input())
print(a)
print(a + 1)
print(a + 2)

# Question 2
# Reads three numbers and prints their sum
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)

# Question 3
# Reads four numbers and prints three times their total sum
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(3 * (a + b + c + d))

# Question 4
# Reads two numbers and calculates a given expression
a = int(input())
b = int(input())
print(3 * (a + b) ** 3 + 275 * (b ** 2) - 127 * a - 41)

# Question 5
# Reads a number, prints the next and the previous numbers
a = int(input())
print("After the number", a, "number:", a + 1)
print("For a", a, "the previous number is", a - 1)

# Question 6
# Reads the side of a cube, prints its volume and surface area
a = int(input())
print("Volume =", a ** 3)
print("Area of the surface =", 6 * (a ** 2))

# Question 7
# Reads two numbers and prints their sum, difference, and product
a = int(input())
b = int(input())
print(a, "+", b, "=", a + b)
print(a, "-", b, "=", a - b)
print(a, "*", b, "=", a * b)

# Question 8
# Reads first term, difference, and position, prints n-th term of an arithmetic progression
a = int(input())
d = int(input())
n = int(input())
print(a + d * (n - 1))

# Question 9
# Reads a number and prints first five multiples separated by '---'
a = int(input())
print(a, 2 * a, 3 * a, 4 * a, 5 * a, sep="---")



# Part 2

# Question 1
# Reads first term, ratio, and position, prints n-th term of a geometric progression
b = int(input())
q = int(input())
n = int(input())
print(b * q ** (n - 1))

# Question 2
# Reads a number and prints its hundreds digit
a = int(input())
print(a // 100)

# Question 3
# Reads n and k, prints how many full groups of n fit into k and the remainder
n = int(input())
k = int(input())
print(k // n)
print(k % n)

# Question 4
# Reads a number and prints half rounded up
n = int(input())
print((n + 1) // 2)

# Question 5
# Reads minutes, prints equivalent in hours and minutes
time = int(input())
print(time, "mins is", time // 60, "hours", time % 60, "minutes.")

# Question 6
# Reads a number and prints how many groups of 4 are needed (rounded up)
n = int(input())
print((n + 3) // 4)

# Question 7
# Reads a three-digit number, prints sum and product of its digits
num= int(input())
a = num // 100
b = (num % 100) // 10
c = num % 10
print("Sum of the numbers is", a + b + c)
print("Product of the numbers is", a * b * c)

# Question 8
# Reads a three-digit number, prints all possible digit arrangements
num= int(input())
a = num // 100
b = (num % 100) // 10
c = num % 10
print(a, b, c, sep="")
print(a, c, b, sep="")
print(b, a, c, sep="")
print(b, c, a, sep="")
print(c, a, b, sep="")
print(c, b, a, sep="")

# Question 9
# Reads a four-digit number and prints each digit with its place value
num = int(input())
a = num // 1000
b = (num % 1000) // 100
c = (num % 100) // 10
d = num % 10
print("The thouthands number is", a)
print("The hundreds number is", b)
print("The tens number is", c)
print("The ones number is  ", d)
