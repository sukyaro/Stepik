import math

# Question 1
# Counts numbers between a and b whose cube ends with 4 or 9
a = int(input())
b = int(input())
total = 0
for i in range(a, b + 1):
        num = i ** 3
        if num % 10 == 4 or num % 10 == 9:
                total += 1
print(total)

# Question 2
# Sums n numbers entered by the user
total = 0
n = int(input())
for i in range(n):
    a = int(input())
    total += a
print(total)

# Question 3
# Sums numbers from 1 to n whose square ends with 2, 5, or 8
total = 0
n = int(input())
for i in range(1, n + 1):
    num = i ** 2
    if num % 10 == 2 or num % 10 == 5 or num % 10 == 8:
        total += i
print(total)

# Question 4
# Calculates factorial of n
counter = 1
n = int(input())
for i in range(1, n + 1):
    counter *= i
print(counter)

# Question 5
# Multiplies 10 non-zero numbers entered by the user
counter = 1
for i in range(10):
    a = int(input())
    if a != 0:
        counter *= a
print(counter)

# Question 6
# Sums all divisors of n
total = 0
n = int(input())
for i in range(n):
    if n % (i + 1) == 0:
        total += (i + 1)
print(total)

# Question 7
# Calculates alternating sum 1 - 2 + 3 - 4 + ... up to n
total = 0
n = int(input())
for i in range(1, n + 1):
    total += (-1) ** (i + 1) * i
print(total)

# Question 8
# Finds the largest and second largest number from n inputs
counter = -1
counter_1 = 0
n = int(input())
for i in range(n):
    a = int(input())
    if a > counter:
        counter_1 = counter
        counter = a
    elif a > counter_1:
        counter_1 = a
print(counter)
print(counter_1)

# Question 9
# Prints first n Fibonacci numbers
num = 0
num_1 = 1
n = int(input())
for i in range(n):
    a = num_1
    num_1 = a + num
    num = a
    print(a, end=" ")
