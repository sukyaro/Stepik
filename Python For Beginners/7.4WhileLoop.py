
# Question 1
# Repeatedly prints input lines until "END" is entered
text = input()
while text != "END":
    print(text)
    text = input()

# Question 2
# Repeatedly prints input lines until "END" or "end" is entered
text = input()
while text != "END" and text != "end":
    print(text)
    text = input()

# Question 3
# Counts the number of inputs until "stop" or "enough" is entered
text = input()
total = 0
while text != "stop" and text != "enough":
    total += 1
    text = input()
print(total)

# Question 4
# Prints numbers repeatedly as long as they are divisible by 7
num = int(input())
while num % 7 == 0:
    print(num)
    num = int(input())

# Question 5
# Sums positive numbers entered until a negative number is input
total = 0
num = int(input())
while num >= 0:
    total += num
    num = int(input())
print(total)

# Question 6
# Counts how many times the mark 5 is entered until an invalid mark is input
total = 0
mark = int(input())
while 0 < mark < 6:
    if mark == 5:
        total += 1
    mark = int(input())
print(total)

# Question 7
# Counts the minimum number of coins needed for a given amount using 25, 10, 5, and 1 denominations
total = 0
num = int(input())
while num > 0:
    if num / 25:
        total += num // 25
        num -= num // 25 * 25
    if num / 10:
        total += num // 10
        num -= num // 10 * 10
    if num / 5:
        total += num // 5
        num -= num // 5 * 5
    if num / 1:
        total += num // 1
        num -= num // 1 * 1
print(total)
