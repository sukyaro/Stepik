
# Question 1
count = 0
p = 1  # mistake number one
for i in range(1, 11):  # mistake number two
    x = int(input())
    if x >= 0:  # mistake number three
        p = p * x
        count = count + 1
if count > 0:
    print(count)  # mistake number four
    print(p)
else:
    print('NO')

# Question 2
mx = -100
s = 0
for i in range(10):  # mistake num 1
    x = int(input())
    if x <= 0:
        s += x  # mistake num 2
    if x > mx and x < 0:  # mistake num 3
        mx = x
if s < 0:
    print(s)
    print(mx)
else:
    print("NO")

# Question 3
s = 0  # mistake num 1
for i in range(1, 8):  # mistake num 2
    n = int(input())  # mistake num 3
    if n % 2 == 0:  # mistake num 4
        s = s + n
print(s)

# Question 4
n = int(input())
max_digit = -1  # mstake num 1
while n > 0:
    digit = n % 10

    if digit % 3 == 0:
        if digit > max_digit:  # mistake num 2
            max_digit = digit  # mistake num 4
    n = n // 10  # mistake num 3
if max_digit == -1:
    print('NO')
else:
    print(max_digit)

# Question 5
n = int(input())
while n > 0:
    last = n % 10
    n //= 10
print(last)

# Question 6
n = int(input())  # mistake num 3
product = 1  # mistake num 1
while n > 0:  # mistake num 2
    digit = n % 10
    product = product * digit
    n //= 10
print(product)