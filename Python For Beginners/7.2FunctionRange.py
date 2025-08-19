# Question 1
# Prints all numbers from m to n inclusive
m = int(input())
n = int(input())

for i in range(m, n + 1):
    print(i)

# Question 2
# Prints numbers from m to n in increasing or decreasing order depending on their values
m = int(input())
n = int(input())
if m < n:
    for i in range(m, n + 1, 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)

# Question 3
# Prints numbers from m to n that are divisible by 17, divisible by both 3 and 5, or end with 9
m = int(input())
n = int(input())
for i in range(m, n + 1):
    if i % 17 == 0 or (i % 3 == 0 and i % 5 == 0) or i % 10 == 9:
        print(i)

# Question 4
# Prints the multiplication table for n from 1 to 10
n = int(input())
for i in range(10):
    print(n, "x", i + 1, "=", n * (i + 1))
