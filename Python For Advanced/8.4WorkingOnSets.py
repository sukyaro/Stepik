
# Question 1
# Finds the sum of the smallest and largest values in the set.
numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
print(min(numbers) + max(numbers))


# Question 2
# Calculates the average of unique numbers in the set.
numbers = {20, 6, 8, 18, 18, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 12, 8, 8, 10, 4, 2, 2, 2, 16, 20}
average = sum(numbers) / len(numbers)
print(average)


# Question 3
# Computes the sum of squares of all unique numbers in the set.
numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
total = 0
for i in numbers:
    total += (i ** 2)
print(total)


# Question 4
# Sorts fruits in reverse alphabetical order and prints each on a new line.
fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
fruits_reverse = sorted(fruits, reverse=True)
print(*fruits_reverse, sep="\n")


# Question 5
# Reads a string and prints the number of distinct characters.
print(len(set(input())))


# Question 6
# Checks if all characters in the input string are unique.
info = input()
if len(info) == len(set(info)):
    print("YES")
else:
    print("NO")


# Question 7
# Checks if every digit from 0–9 appears in at least one of the two inputs.
info_1 = set([int(i) for i in input()])
info_2 = set([int(i) for i in input()])

flag = True
for i in range(10):
    if i not in info_1:
        if i not in info_2:
            flag = False

if flag == True:
    print("YES")
else:
    print("NO")


# Question 8
# Checks if both inputs contain exactly the same set of digits.
info_1 = set([int(i) for i in input()])
info_2 = set([int(i) for i in input()])

if info_1 == info_2:
    print("YES")
else:
    print("NO")


# Question 9
# Reads three words and checks if they all consist of the same unique characters.
data = input().split()
info_1 = set(data[0])
info_2 = set(data[1])
info_3 = set(data[2])

if info_1 == info_2 and info_1 == info_3 and info_2 == info_3:
    print("YES")
else:
    print("NO")
