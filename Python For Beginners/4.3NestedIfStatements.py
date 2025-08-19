
# Question 1
# Reads two numbers and compares them: prints "YES" if first < second, "NO" if first > second, "Don't know" if equal
n = int(input())
k = int(input())
if n == k:
    print("Don't know")
elif n < k:
    print("YES")
elif n > k:
    print("NO")

# Question 2
# Reads three numbers as triangle sides and prints the type of triangle
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print("Equilateral")
elif a == b != c or a != b == c or a == c != b:
    print("Isosceles")
else:
    print("Different-sided")

# Question 3
# Reads three numbers and prints the middle one (the median)
a = int(input())
b = int(input())
c = int(input())
if a > b > c or c > b > a:
    print(b)
elif b > a > c or c > a > b:
    print(a)
elif a > c > b or b > c > a:
    print(c)

# Question 4
# Reads a month number and prints how many days it has
a = int(input())
if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
    print("31")
elif a == 2:
    print("28")
else:
    print("30")

# Question 5
# Reads a weight and prints the weight category
a = int(input())
if a < 60:
    print("Light weight")
elif 60 <= a < 64:
    print("First middle weight")
else:
    print("Middle weight")

# Question 6
# Reads two numbers and an operator, performs the operation (with division by zero check)
a = int(input())
b = int(input())
c = input()
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif b == 0 and c == "/":
    print("You cant divide by 0!")
elif c == "/":
    print(a / b)
else:
    print("Wrong operation")

# Question 7
# Reads two colours and prints the resulting mix (basic colour mixing)
a = input()
b = input()
if (a == "red" and b == "blue") or (a == "blue" and b == "red"):
    print("purple")
elif (a == "red" and b == "yellow") or (a == "yellow" and b == "red"):
    print("orange")
elif (a == "blue" and b == "yellow") or (a == "yellow" and b == "blue"):
    print("green")
elif a == "red" and b == "red":
    print("red")
elif a == "blue" and b == "blue":
    print("blue")
elif a == "yellow" and b == "yellow":
    print("yellow")
else:
    print("colour error")

# Question 8
# Reads a roulette number and prints its colour (green, red, black) or error if invalid
a = int(input())
if a == 0:
    print("green")
elif 1 <= a <= 10 or 19 <= a <= 28:
    if a % 2 == 0:
        print("black")
    else:
        print("red")
elif 11 <= a <= 18 or 29 <= a <= 36:
    if a % 2 == 0:
        print("red")
    else:
        print("black")
else:
    print("colour error")

# Question 9
# Reads two intervals and prints their intersection, or "empty set" if they don't overlap
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if b1 == a2:
    print(a2)
elif b2 == a1:
    print(a1)
elif a1 <= a2 < b1 < b2:
    print(a2, b1)
elif a2 <= a1 < b2 < b1:
    print(a1, b2)
elif a2 < a1 < b1 <= b2:
    print(a1, b1)
elif a1 < a2 < b2 <= b1:
    print(a2, b2)
elif a2 < a1 < b1 == b2:
    print(a1, b1)
elif a1 < a2 < b1 == b2:
    print(a2, b2)
elif a1 == a2 and b1 == b2:
    print(a1, b1)
elif b1 < a2 or b2 < a1:
    print("empty set")