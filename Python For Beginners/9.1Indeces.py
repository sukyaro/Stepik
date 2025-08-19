# Question 1
# Prints the 8th character of the string
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[7])

# Question 2
# Prints every second character of the input string starting from the first
n = input()
for i in range(0, len(n), 2):
    print(n[i])

# Question 3
# Prints the input string in reverse order
n = input()
for i in range(1, len(n) + 1):
    print(n[-i])

# Question 4
# Prints the first letter of the second, first, and third input strings together
a = input()
b = input()
c = input()
print(b[0], a[0], c[0], sep="")

# Question 5
# Calculates and prints the sum of digits of the input number
a = int(input())
total = 0
while a > 0:
    l_d = a % 10
    total += l_d
    a //= 10
print(total)

# Question 6
# Checks if the input string contains any digits and prints "Number" or "No Numbers"
n = input()
counter = 0
for i in range(len(n)):
    if n[i] in "0123456789":
        counter += 1
if counter > 0:
    print("Number")
else:
    print("No Numbers")

# Question 7
# Counts the number of '+' and '*' symbols in the input string
n = input()
counter_0 = 0
counter_1 = 0
for i in n:
    if i == "+":
        counter_0 += 1
    if i == "*":
        counter_1 += 1
print(f"The symbol + is in the string {counter_0} times")
print(f"The symbol * is in the string {counter_1} times")

# Question 8
# Counts the number of consecutive identical characters in the input string
n = input()
counter = 0
for i in range(len(n) - 1):
    if n[i] == n[i + 1]:
        counter += 1
print(counter)

# Question 9
# Counts the number of vowels and consonants in the input string (Cyrillic letters)
n = input()
counter_0 = 0
counter_1 = 0
for i in n:
    if i.upper() in "AEIOU":
        counter_0 += 1
    if i.upper() in "BCDFGHJKLMNPQRSTVWXYZ":
        counter_1 += 1
print(f"The number of vowels letters is {counter_0}")
print(f"The number of consonant letters is {counter_1}")

# Question 10
# Converts the input number to binary and prints it
n = int(input())
lis = []
while n > 0:
    lis.append(n % 2)
    n = n // 2
lis.reverse()
for i in range(len(lis)):
    print(lis[i], end="")
