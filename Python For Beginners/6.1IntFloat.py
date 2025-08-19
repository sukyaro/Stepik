
# Question 1
# Calculates the area of a triangle given base and height
a = float(input())
b = float(input())
print(1 / 2 * a * b)

# Question 2
# Calculates the time for two objects moving toward each other to meet
s = float(input())
v1 = float(input())
v2 = float(input())
print(s / (v1 + v2))

# Question 3
# Prints the reciprocal of a number, or a message if the number is 0
a = float(input())
if a == 0:
    print("The backwards number doesnt exist")
else:
    print(a ** -1)

# Question 4
# Converts Fahrenheit to Celsius
f = float(input())
print(5 / 9 * (f - 32))

# Question 5
# Calculates total cost based on number of items with different rates
n = int(input())
if 1 <= n <= 2:
    print(n * 10.5)
else:
    print(2 * 10.5 + (n - 2) * 4)

# Question 6
# Extracts the first digit after the decimal point of a float
a = float(input())
b = int(a)
c = ((a - b) * 10)
print(int(c))

# Question 7
# Prints the fractional part of a number
a = float(input())
print(a - int(a))

# Question 8
# Finds the smallest and largest of five numbers
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
print("Smallest number =", min(num1, num2, num3, num4, num5))
print("Biggest number =", max(num1, num2, num3, num4, num5))

# Question 9
# Prints the numbers in order from largest to smallest
a = int(input())
b = int(input())
c = int(input())
print(max(a, b, c))
print(a + b + c - max(a, b, c) - min(a, b, c))
print(min(a, b, c))

# Question 10
# Checks if a three-digit number has the middle digit equal to the average of the other two
a = int(input())
num1 = a // 100
num2 = (a % 100) // 10
num3 = a % 10
if max(num1, num2, num3) - min(num1, num2, num3) == num1 + num2 + num3 - max(num1, num2, num3) - min(num1, num2, num3):
    print("Interesting number")
else:
    print("Not interesting number")

# Question 11
# Calculates the sum of the absolute values of five numbers
a1 = float(input())
a2 = float(input())
a3 = float(input())
a4 = float(input())
a5 = float(input())
print(abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5))

# Question 12
# Calculates the Manhattan distance between two points
p1 = int(input())
p2 = int(input())
q1 = int(input())
q2 = int(input())
print(abs(p1 - q1) + abs(p2 - q2))
