
# Question 1
# Reads two inputs and checks if they are equal, prints a message accordingly
a = input()
b = input()
if a == b:
    print("Passwords dont match")
else:
    print("The password is accepted")

# Question 2
# Reads a number and prints if it is even or odd
a = int(input())
if a % 2 == 0:
    print("Even")
else:
    print("Odd")

# Question 3
# Reads a 4-digit number and checks if (1st + 3rd) = (2nd - 4th)
a = int(input())
q = a // 1000
w = (a % 1000) // 100
e = (a % 100) // 10
r = a % 10
if q + e == w - r:
    print("YES")
else:
    print("NO")

# Question 4
# Reads an age and checks if access is allowed or denied
a = int(input())
if 0 < a < 18:
    print("Access is denied")
else:
    print("Access is given")

# Question 5
# Reads three numbers and checks if they form an arithmetic sequence
a = int(input())
b = int(input())
c = int(input())
if b - a == c - b:
    print("YES")
else:
    print("NO")

# Question 6
# Reads two numbers and prints the smaller one
a = int(input())
b = int(input())
if a < b:
    print(a)
else:
    print(b)

# Question 7
# Reads four numbers and prints the smallest one
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a < b:
    f = a
else:
    f = b
if c < d:
    m = c
else:
    m = d
if f < m:
    print(f)
else:
    print(m)

# Question 8
# Reads an age and prints the life stage (childhood, teenager, adult, old)
a = int(input())
if a <= 13:
    print("childhood")
if 14 <= a <= 24:
    print("teenager")
if 25 <= a <= 59:
    print("adult")
if a >= 60:
    print("old")

# Question 9
# Reads three numbers, replaces negatives with 0, then prints their sum
a = int(input())
b = int(input())
c = int(input())
if a < 0:
    q = 0
else:
    q = a
if b < 0:
    w = 0
else:
    w = b
if c < 0:
    e = 0
else:
    e = c
print(q + w + e)