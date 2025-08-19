
# Question 1
# Splits input by spaces and prints each word on a new line
a = input().split()
for i in a:
    print(i)

# Question 2
# Prints the first letter of each word from input followed by a dot
a = input().split()
for i in range(len(a)):
    print(a[i][0], end=".")

# Question 3
# Splits input by backslashes and prints each part on a new line
print(*input().split("\\"), sep="\n")

# Question 4
# Converts input numbers to integers and prints that many plus signs for each
a = input().split()
for i in a:
    print(int(i) * "+")

# Question 5
# Checks if input is a valid IPv4 address (all parts between 0 and 255)
a = input().split(".")
b = True
for i in a:
    if int(i) > 255 or int(i) < 0:
        b = False

if b == True:
    print("YES")
else:
    print("NO")

# Question 6
# Inserts the second input string between each character of the first input
a = list(input())
print(input().join(a))

# Question 7
# Counts the number of duplicate words in the input
a = input().split()
counter = 0
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] == a[j] and i != j:
            counter += 1
print(counter // 2)

