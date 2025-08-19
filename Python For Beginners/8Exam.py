
# Question 1
# Calculates the sum of even digits of the input number
n = int(input())  # mistake num 1
s = 0
while n > 0:  # mistake num 2
    if n % 2 == 0:  # mistake num 3
        s += n % 10  # mistake num 4
    n //= 10
print(s)

# Question 2
# Counts numbers divisible by 4 from 8 inputs and finds the maximum among them
n = 8  # mistake num 1
count = 0
maximum = -10 ** 6 - 1  # mistake 3
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:  # mistake num 2
        count += 1
        if x > maximum:  # mistake 4
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

# Question 3
# Counts odd numbers from 4 inputs and finds the maximum among them
n = 4
count = 0
maximum = -10 ** 6 - 1
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

# Question 4
# Prints a rectangle of asterisks with hollow inside
n = int(input())

for i in range(n):
    if i == 0 or i == n - 1:
        print('*' * 19)
    else:
        print('*' + ' ' * 17 + '*')

# Question 5
# Prints the last digit of the number when it becomes less than or equal to 100
n = int(input())
while n > 100:
    l_d = n % 10
    n //= 10
print(l_d)

# Question 6
# Performs multiple digit-based calculations on the number:
# counts 3s, counts occurrences of last digit, counts even digits, sums digits >5,
# multiplies digits >7, counts 0s and 5s
n = int(input())
num_of_3 = 0
l_d_r = n % 10
num_of_l_d_r = 0
num_of_even_nums = 0
sum_of_num_more5 = 0
multiply_of_nums_more7 = 1
times_num_from_0_to_5 = 0

while n > 0:
    l_d = n % 10
    if l_d == 3:
        num_of_3 += 1
    if l_d == l_d_r:
        num_of_l_d_r += 1
    if l_d % 2 == 0:
        num_of_even_nums += 1
    if l_d > 5:
        sum_of_num_more5 += l_d
    if l_d > 7:
        multiply_of_nums_more7 *= l_d
    if l_d == 0 or l_d == 5:
        times_num_from_0_to_5 += 1
    n //= 10

print(num_of_3)
print(num_of_l_d_r)
print(num_of_even_nums)
print(sum_of_num_more5)
print(multiply_of_nums_more7)
print(times_num_from_0_to_5)
