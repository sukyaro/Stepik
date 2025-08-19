
# Question 1
# Reads a number and checks if it is between 0 and 16 inclusive
a = int(input())
if -1 < a < 17:
    print("Withing the limit")
else:
    print("Not withing the limit")

# Question 2
# Reads a number and checks if it is ≤ -3 or ≥ 7
a = int(input())
if a <= -3 or a >= 7:
    print("Withing the limit")
else:
    print("Not withing the limit")

# Question 3
# Reads a number and checks if it is in (-30, -2] or (7, 25]
a = int(input())
if -30 < a <= -2 or 7 < a <= 25:
    print("Withing the limit")
else:
    print("Not withing the limit")

# Question 4
# Reads a number and checks if it is a 4-digit number divisible by 7 or 17
a = int(input())
if (a % 7 == 0 or a % 17 == 0) and (999 < a < 10000):
    print("YES")
else:
    print("NO")

# Question 5
# Reads three numbers and checks if they can be triangle sides
a = int(input())
b = int(input())
c = int(input())
if a + b > c and b + c > a and a + c > b:
    print("YES")
else:
    print("NO")

# Question 6
# Reads a year and checks if it is a leap year
a = int(input())
if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
    print("YES")
else:
    print("NO")

# Question 7
# Reads coordinates and checks if a rook can move from one position to another
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (c == a and 1 <= d <= 8) or (b == d and 1 <= c <=8):
    print("YES")
else:
    print("NO")

# Question 8
# Reads coordinates and checks if a king can move from one position to another
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if ((c == a + 1 or c == a - 1) and d == b) or ((d == b + 1 or d == b -1) and c == a) or ((c == a + 1 or c == a - 1) and (d == b + 1 or d == b - 1)):
    print("YES")
else:
    print("NO")