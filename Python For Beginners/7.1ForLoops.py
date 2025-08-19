
# Question 1
# Prints "Python is awesome!" 10 times
for i in range(10):
    print("Python is awesome!")

# Question 2
# Prints a specific pattern of strings with loops and single print statements
for i in range(6):
    print("AAA")
for i in range(5):
    print("BBBB")
print("E")
for i in range(9):
    print("TTTTT")
print("G")

# Question 3
# Prints the input string a given number of times
a = input()
b = int(input())
for i in range(b):
    print(a)

# Question 4
# Prints a line of asterisks n times
n = int(input())
for i in range(n):
    print("*******************")

# Question 5
# Prints the input string 10 times with the current index number
a = input()
for i in range(10):
    print(i, a)

# Question 6
# Prints the square of each number from 0 to n
n = int(input())
for i in range(n + 1):
    print("A square of the number", i, "is", i ** 2)

# Question 7
# Prints a triangle of asterisks with decreasing length
n = int(input())
for i in range(n):
    print((n - i) * "*")

# Question 8
# Prints the value of an amount m growing by p% over n periods
m = int(input())
p = int(input())
n = int(input())
for i in range(n):
    print(i + 1, m * (1 + p / 100) ** i)
