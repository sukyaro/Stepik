
# Question 1
# Reads a number and checks if its last two digits are both zero
a = int(input())
num1 = a % 10
num2 = (a % 100) // 10
if num1 == num2 == 0:
    print("YES")
else:
    print("NO")

# Question 2
# Reads coordinates of two chessboard cells and checks if they are the same colour
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if (a1 % 2 != 0 and b1 % 2 != 0) or (a1 % 2 == 0 and b1 % 2 == 0):
    if (a2 % 2 != 0 and b2 % 2 != 0) or (a2 % 2 == 0 and b2 % 2 == 0):
        print("YES")
    else:
        print("NO")
elif (a1 % 2 != 0 and b1 % 2 == 0) or (a1 % 2 == 0 and b1 % 2 != 0):
    if (a2 % 2 != 0 and b2 % 2 == 0) or (a2 % 2 == 0 and b2 % 2 != 0):
        print("YES")
    else:
        print("NO")

# Question 3
# Reads age and sex, prints YES if female aged between 10 and 15
years = int(input())
sex = input()
if 10 <= years <= 15 and sex == "f":
    print("YES")
else:
    print("NO")

# Question 4
# Reads a number 1–10 and prints its Roman numeral, otherwise prints error
a = int(input())
if a == 1:
    print("I")
elif a == 2:
    print("II")
elif a == 3:
    print("III")
elif a == 4:
    print("IV")
elif a == 5:
    print("V")
elif a == 6:
    print("VI")
elif a == 7:
    print("VII")
elif a == 8:
    print("VIII")
elif a == 9:
    print("IX")
elif a == 10:
    print("X")
else:
    print("error")

# Question 5
# Reads a number and checks conditions to print YES or NO (based on parity and range)
a = int(input())
if a % 2 != 0:
    print("YES")
elif 2 <= a <= 5:
    print("NO")
elif 6 <= a <= 20:
    print("YES")
elif a % 2 == 0 and a > 20:
    print("NO")

# Question 6
# Reads two chessboard positions and checks if they lie on the same diagonal
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a1 == b1 and a2 == b2:
    print("YES")
elif a1 == b2 and b1 == a2:
    print("YES")
elif (a2 == a1 + 1 and b2 == b1 - 1) or (a2 == a1 + 2 and b2 == b1 - 2) or (a2 == a2 == a1 + 3 and b2 == b1 - 3) or (a2 == a1 + 4 and b2 == b1 - 4) or (a2 == a1 + 5 and b2 == b1 - 5) or (a2 == a1 + 6 and b2 == b1 - 6) or (a2 == a1 + 8 and b2 == b1 - 8):
    print("YES")
elif (a2 == a1 - 1 and b2 == b1 + 1) or (a2 == a1 - 2 and b2 == b1 + 2) or (a2 == a2 == a1 - 3 and b2 == b1 + 3) or (a2 == a1 - 4 and b2 == b1 + 4) or (a2 == a1 - 5 and b2 == b1 + 5) or (a2 == a1 - 6 and b2 == b1 + 6) or (a2 == a1 - 8 and b2 == b1 + 8):
    print("YES")
elif a2 == a1 - 1 and b2 == b1 - 1:
    print("YES")
else:
    print("NO")

# Question 7
# Reads two chessboard positions and checks if a knight can move from one to the other
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if (a2 == a1 + 2 or a2 == a1 - 2) and (b2 == b1 + 1 or b2 == b1 - 1):
    print("YES")
elif (a2 == a1 + 1 or a2 == a1 - 1) and (b2 == b1 + 2 or b2 == b1 - 2):
    print("YES")
else:
    print("NO")

# Question 8
# Reads two chessboard positions and checks if a queen can move from one to the other
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if a1 == a2 or b1 == b2:
    print("YES")
elif a1 == b1 and a2 == b2:
    print("YES")
elif a1 == b2 and b1 == a2:
    print("YES")
elif (a2 == a1 + 1 and b2 == b1 - 1) or (a2 == a1 + 2 and b2 == b1 - 2) or (a2 == a2 == a1 + 3 and b2 == b1 - 3) or (a2 == a1 + 4 and b2 == b1 - 4) or (a2 == a1 + 5 and b2 == b1 - 5) or (a2 == a1 + 6 and b2 == b1 - 6) or (a2 == a1 + 8 and b2 == b1 - 8):
    print("YES")
elif (a2 == a1 - 1 and b2 == b1 + 1) or (a2 == a1 - 2 and b2 == b1 + 2) or (a2 == a2 == a1 - 3 and b2 == b1 + 3) or (a2 == a1 - 4 and b2 == b1 + 4) or (a2 == a1 - 5 and b2 == b1 + 5) or (a2 == a1 - 6 and b2 == b1 + 6) or (a2 == a1 - 8 and b2 == b1 + 8):
    print("YES")
elif a2 == a1 - 1 and b2 == b1 - 1:
    print("YES")
elif (a2 == a1 + 1 and b2 == b1 + 1) or (a2 == a1 + 2 and b2 == b1 + 2) or (a2 == a1 + 3 and b2 == b1 + 3) or (a2 == a1 + 4 and b2 == b1 + 4) or (a2 == a1 + 5 and b2 == b1 + 5) or (a2 == a1 + 6 and b2 == b1 + 6) or (a2 == a1 + 7 and b2 == b1 + 7) or (a2 == a1 + 8 and b2 == b1 + 8):
    print("YES")
elif (a2 == a1 - 1 and b2 == b1 - 1) or (a2 == a1 - 2 and b2 == b1 - 2) or (a2 == a1 - 3 and b2 == b1 - 3) or (a2 == a1 - 4 and b2 == b1 - 4) or (a2 == a1 - 5 and b2 == b1 - 5) or (a2 == a1 - 6 and b2 == b1 - 6) or (a2 == a1 - 7 and b2 == b1 - 7) or (a2 == a1 - 8 and b2 == b1 - 8):
    print("YES")
else:
    print("NO")