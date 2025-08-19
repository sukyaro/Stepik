
# Part 1
# Question 1
# Prints the number n, three times per row, for n rows
n = int(input())

for i in range(n):
    for a in range(3):
        print(n, end=" ")
    print()

# Question 2
# Prints numbers from 1 to n, each number printed 5 times per row
n = int(input())

for i in range(n):
    for a in range(5):
        print(i + 1, end=" ")
    print()

# Question 3
# Prints an addition table: each row i adds with numbers 1 to 9
n = int(input())

for i in range(n):
    for a in range(9):
        print((i + 1), "+", (a + 1), "=", (i + 1) + (a + 1))
    print()

# Question 4
# Prints a pyramid of asterisks with height based on input a
a = int(input())
b = (a + 1) // 2

for i in range(b):
    print((i + 1) * "*")

for i in range(a - b, 0, -1):
    print(i * "*")

# Question 5
# Prints rows of increasing repeated digits, row i has i+1 repetitions of digit i+1
n = int(input())

for i in range(n):
    for a in range(i + 1):
        print(i + 1, end="")
    print()


# Part 2
# Question 1
# Prints numbers sequentially in a triangular pattern
n = int(input())
cur = 1

for i in range(n):
    for _ in range(i + 1):
        print(cur, end=" ")
        cur += 1
    print()

# Question 2
# Prints a pyramid pattern with mirrored numbers
n = int(input())

for i in range(n):
    for a in range(i):
        print(a + 1, end="")
    for j in range(i, -1, -1):
        print(j + 1, end="")
    print()

# Question 3
# Finds the number with the maximum sum of divisors in the range a to b
a = int(input())
b = int(input())
number = 0
num_of = 0

for i in range(a, b + 1):
    q = 0
    for j in range(1, i + 1):
        if i % j == 0:
            q += j
        if q >= num_of:
            num_of = q
            number = i

print(number, num_of)

# Question 4
# Prints each number from 1 to n with "+" symbols equal to its number of divisors
n = int(input())

for i in range(1, n + 1):
    counter = 0
    for a in range(1, i + 1):
        if i % a == 0:
            counter += 1
    print(str(i) + counter * "+")

# Question 5
# Calculates the repeated sum of digits of n three times
n = int(input())

for i in range(3):
    total_1 = 0
    while n > 0:
        l_d = n % 10
        total_1 += l_d
        n //= 10
    n = total_1
print(total_1)

# Question 6
# Calculates the sum of factorials from 1! to n!
n = int(input())
total = 0

for i in range(n):
    q = 1
    for a in range(1, i + 2):
        q *= a
    total += q
print(total)

# Question 7
# Prints all prime numbers in the range from a to b
a = int(input())
b = int(input())

for i in range(a, b + 1):
    if i == 1:
        continue
    for q in range(2, i):
        if i % q == 0:
            break
    else:
        print(i)
