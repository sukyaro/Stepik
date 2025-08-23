
from math import *


# Part 1
# Question 1
# Appends 7000 to the nested list inside list1.
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

# Question 2
# Extends a nested sublist inside list1 with ['h', 'i', 'j'].
list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
sub_list = ['h', 'i', 'j']
list1[2][1][2].extend(sub_list)
print(list1)

# Question 3
# Finds and prints the maximum number in a 2D list.
list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
max = -1
for x in list1:
    for j in x:
        if j > max:
            max = j

print(max)

# Question 4
# Reverses each sublist inside list1.
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
for x in range(len(list1)):
    list1[x].reverse()

print(list1)

# Question 5
# Calculates and prints the average of all numbers in a 2D list.
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0
for x in list1:
    total += sum(x)
    counter += len(x)

print(total / counter)


# Part 2
# Question 1
# Creates an n×n matrix with values from 1 to n in each row.
n = int(input())
lis = [n * [0] for _ in range(n)]
for x in range(len(lis)):
    for j in range(len(lis)):
        lis[x][j] = j + 1
    print(lis[x])

# Question 2
# Prints a triangular number pattern from 1 up to n.
n, count = int(input()), 1
for i in range(n):
    print(*[[x for x in range(1, count + 1)]])
    count += 1

# Question 3
# Generates the nth row of Pascal’s triangle.
n, m, a = int(input()), 0, []
for i in range(n):
    a.append(int(factorial(n) / (factorial(m) * factorial(n - m))))
    m += 1
a.append(1)
print(a)

# Question 4
# Prints Pascal’s triangle up to row n.
n, m, a, count = int(input()), 0, [], 0
for j in range(n):
    for i in range(count):
        a.append(int(factorial(count) / (factorial(m) * factorial(count - m))))
        m += 1
    m = 0
    a.append(1)
    count += 1
    print(*a)
    a = []

# Question 5
# Groups consecutive identical elements from input into sublists.
a, pack = input().split(), []
pack.append([a[0]])
for i in range(1, len(a)):
    if a[i] in pack[-1]:
        pack[-1].append(a[i])
    else:
        pack.append([a[i]])

print(pack)

# Question 6
# Splits a list into chunks of a given size.
def chunked(sim, size):
    a, frm = [], 0
    if len(sim) % size != 0:
        b = len(sim) // size + 1
    else:
        b = len(sim) // size
    for i in range(b):
        a.append(sim[frm:size * (i + 1)])
        frm = size * (i + 1)
    return a

print(chunked(input().split(), int(input())))

# Question 7
# Generates all possible contiguous sublists of the input list.
a, my_list, ad = input().split(), [[]], []

for i in range(len(a)):
    for j in range(len(a)):
        ad = a[j:i+j+1]
        if len(ad) == i + 1:
            my_list.append(ad)
    
print(my_list)
