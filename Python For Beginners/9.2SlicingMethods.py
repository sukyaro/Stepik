# Part 1
# Question 1
# Checks if both words in the input (separated by a space) start with a capital letter
a = input()
b = a.find(" ")
if a[:b + 1] == a[:b + 1].capitalize() and a[b + 1:] == a[b + 1:].capitalize():
    print("YES")
else:
    print("NO")

# Question 2
# Swaps the case of all letters in the input string
a = input()
print(a.swapcase())

# Question 3
# Checks if the word "good" (case insensitive) is in the input string
a = input()
a = a.lower()
if "good" in a:
    print("YES")
else:
    print("NO")

# Question 4
# Counts the number of lowercase letters in the input that are not digits
a = input()
total = 0
for i in range(len(a)):
    if a[i] in "0123456789":
        continue
    if a[i] == a[i].lower():
        total += 1
print(total)


# Part 2
# Question 1
# Counts the number of words in the input string (assuming words are separated by spaces)
a = input()
print(a.count(" ") + 1)

# Question 2
# Counts occurrences of specific letters in the input string (case insensitive) for given names
a = input()
a = a.lower()
print("Mark:", a.count("k"))
print("Jonathan:", a.count("a"))
print("Elizabeth:", a.count("i"))
print("Donnald:", a.count("n"))

# Question 3
# Counts how many input strings (from a lines) contain "11" more than 2 times
a = int(input())
total = 0
for i in range(a):
    b = input()
    if b.count("11") > 2:
        total += 1
print(total)

# Question 4
# Checks if the input string ends with ".com" or ".uk"
a = input()
if a.endswith(".com") == True or a.endswith(".uk") == True:
    print("YES")
else:
    print("NO")

# Question 5
# Finds the first and last occurrence of "f" in the input string, prints positions or "NO" if absent
a = input()
if a.find("f") != -1 and a.find("f") == a.rfind("f"):
    print(a.find("f"))
elif a.find("f") != -1:
        print(a.find("f"), a.rfind("f"))
else:
    print("NO")

# Question 6
# Prints the input string without the part between the first and last "h" (inclusive)
a = input()
print(a[:a.find("h")], a[a.rfind("h") + 1:], sep="")
