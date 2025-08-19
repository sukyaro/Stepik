
# Part 1
# Question 1
# Prints the length, last element, reversed list, checks for 5 and 17, deletes first and last elements
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

print(len(numbers))
print(numbers[-1])
print(numbers[::-1])

if 5 and 17 in numbers:
    print("YES")
else:
    print("NO")

del numbers[0]
del numbers[-1]
print(numbers)

# Question 2
# Reads n strings from input and stores them in a list
n = int(input())
a = []

for i in range(n):
    b = input()
    a.append(b)

print(a)

# Question 3
# Creates a list of strings with repeated letters 'a' to 'z'
a = []
for i in range(26):
    a.append(chr(97 + i) * (i + 1))
print(a)

# Question 4
# Reads n numbers, cubes them, and stores in a list
a = []
n = int(input())

for i in range(n):
    b = int(input())
    a.append(b ** 3)

print(a)

# Question 5
# Reads n numbers, adds each to previous number, removes first element
a = []
c = 0
n = int(input())

for i in range(n):
    b = int(input())
    a.append(b + c)
    c = b

del a[0]
print(a)

# Question 6
# Reads numbers into a list, prints every second element
a = []

for i in range(int(input())):
    b = int(input())
    a.append(b)

a = a[::2]
print(a)

# Question 7
# Reads n strings and prints k-th character of each if length is enough
a = []
n = int(input())

for i in range(n):
    b = input()
    a.append(b)

k = int(input())
for i in range(len(a)):
    if len(a[i]) < k:
        pass
    else:
        print(a[i][k - 1], end="")

# Question 8
# Reads n strings and combines all characters into a single list
a = []
n = int(input())

for i in range(n):
    b = input()
    a.extend(b)

print(a)


# Part 2
# Question 1
# Modifies a list by removing, inserting, appending, repeating, and inserting elements
numbers = [8, 9, 10, 11]
numbers.pop(1)
numbers.insert(1, 17)
numbers.append(4)
numbers.append(5)
numbers.append(6)
numbers.pop(0)
numbers *= 2
numbers.insert(3, 25)
print(numbers)

# Question 2
# Swaps the maximum and minimum values in a list of integers
a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
    a[i] = a[i]
 
b, c = max(a), min(a)
d, e = a.index(max(a)), a.index(min(a))

a[d] = c
a[e] = b
print(*a)

# Question 3
# Counts how many times English articles appear in a sentence
a = input().lower().split()
print("Sum of the articles:", a.count("a") + a.count("an") + a.count("the"))

# Question 4
# Reads n lines of text, removes trailing '#' and prints the cleaned lines
a = input().lstrip("#")
d = []
for i in range(int(a)):
    b = input()
    if "#" in b:
        c = b.rfind("#")
        d.append(b[:c].rstrip())
    else:
        d.append(b.rstrip())
print(*d, sep="\n")

# Question 5
# Reads a list of integers, prints them sorted ascending and descending
a = input().split()
b = []
for i in a:
    i = int(i)
    b.append(i)
b.sort()
print(*b)
b.sort(reverse=True)
print(*b)

# Question 6
# Reads n strings and prints them sorted alphabetically
print(*sorted([input() for _ in range(int(input()))]), sep='\n')
