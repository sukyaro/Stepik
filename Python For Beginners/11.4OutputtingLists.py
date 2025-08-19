# Question 1
# Squares each number in the list and prints the sum of all squares
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2
print(sum(numbers))

# Question 2
# Reads n integers, prints them, then prints (number^2 + 2*number + 1) for each
n = int(input())
b = []
for i in range(n):
    a = int(input())
    b.append(a)

print(*b, sep="\n")
print()

for i in b:
    print(i ** 2 + 2 * i + 1)

# Question 3
# Reads n strings and prints only unique strings, keeping order
n = int(input())
b = []
for i in range(n):
    a = input()
    if a not in b:
        b.append(a)


print(*b, sep="\n")

# Question 4
# Reads n strings, then prints strings containing a given substring (case-insensitive)
n = int(input())
a = []

for i in range(n):
    b = input()
    a.append(b)

n = input()

for i in range(len(a)):
    if n.lower() in a[i].lower():
        print(a[i])

# Question 5
# Reads n strings, then filters and prints strings containing all substrings from another list (case-insensitive)
n = int(input())
a = []

for i in range(n):
    b = input()
    a.append(b)

n = int(input())
d = []
d_1 = []

for i in range(n):
    b = input()
    d.append(b)

for i in range(len(a)):
    counter = 0
    for j in range(len(d)):
        if d[j].lower() in a[i].lower():
            counter += 1
        if counter == len(d):
            d_1.append(a[i])
print(*d_1, sep="\n")

# Question 6
# Reads n integers and prints negative numbers first, then zeros, then positive numbers
n = int(input())
a = []

for i in range(n):
    b = int(input())
    a.append(b)

for i in a:
    if i < 0:
        print(i)

for i in a:
    if i == 0:
        print(i)

for i in a:
    if i > 0:
        print(i)