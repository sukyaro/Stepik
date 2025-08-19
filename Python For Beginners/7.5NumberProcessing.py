# Question 1
# Prints each digit of a number on a new line starting from the last digit
num = int(input())
while num != 0:
    l_d = num % 10
    print(l_d)
    num = num // 10

# Question 2
# Prints the digits of a number in reverse on the same line
num = int(input())
while num != 0:
    l_d = num % 10
    print(l_d, end="")
    num = num // 10

# Question 3
# Finds and prints the maximum and minimum digit of a number
num = int(input())
counter = -1
counter_1 = 9
while num > 0:
    l_d = num % 10
    if l_d > counter:
        counter = l_d
    if l_d < counter_1:
        counter_1 = l_d
    num = num // 10
print("The max number is", counter)
print("The min number is", counter_1)

# Question 4
# Prints the first digit (most significant) of a number
num = int(input())
while num > 9:
    l_d = num % 10
    num //= 10
print(l_d)

# Question 5
# Checks if all digits of a number are the same
num = int(input())
n = num % 10
a = True
while num != 0:
    l_d = num % 10
    if l_d != n:
        a = False
    num //= 10
if a:
    print("YES")
else:
    print("NO")

# Question 6
# Checks if the digits of a number are in non-decreasing order from left to right
num = int(input())
coun = -1
a = True
while num != 0:
    l_d = num % 10
    if l_d >= coun:
        coun = l_d
    else:
        a = False
    num //= 10
if a:
    print("YES")
else:
    print("NO")
