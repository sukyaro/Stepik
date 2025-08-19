
# Question 1
# Finds and prints the smallest divisor of a number greater than 1
num = int(input())
for i in range(2, num + 1):
    if num % i == 0:
        print(i)
        break

# Question 2
# Prints all numbers from 1 to num, skipping ranges 5-9, 17-37, and 78-87
num = int(input())
for i in range(1, num + 1):
    if 5 <= i <= 9:
        continue
    elif 17 <= i <= 37:
        continue
    elif 78 <= i <= 87:
        continue
    print(i)
