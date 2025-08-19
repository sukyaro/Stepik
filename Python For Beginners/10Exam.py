# Question 1
# Prints the length of the string
s = 'Python rocks!'
print(len(s))

# Question 2
# Prints the 4th character of the string (index 3)
s = 'Python rocks!'
print(s[3])

# Question 3
# Prints characters from index 1 to 4 (slice)
s = 'Python rocks!'
print(s[1:5])

# Question 4
# Removes leading and trailing spaces from the string
s = '    Python rocks!     '
print(s.strip())

# Question 5
# Converts the string to uppercase
s = 'Python rocks!'
print(s.upper())

# Question 6
# Prints all characters except every 3rd character (indexes divisible by 3)
a = input()
for i in range(len(a)):
    if i % 3 == 0:
        continue
    else:
        print(a[i], end="")

# Question 7
# Same as Question 7: prints all characters except every 3rd one
a = input()
for i in range(len(a)):
    if i % 3 == 0:
        continue
    else:
        print(a[i], end="")

# Question 8
# Removes all "@" symbols from the input string
a = input().replace("@", "")
print(a)

# Question 9
# Finds the second occurrence of "f" or returns special values if less than 2
a = input()
if a.count("f") == 0:
    print(-2)
elif a.count("f") == 1:
    print(-1)
elif a.count("f") == 2:
    print(a.rfind("f"))
else:
    while a.count("f") != 2:
        a = a[:-1]
    print(a.rfind("f"))

# Question 10
# Reverses the substring between the first and last occurrence of "h" in the input
a = input()
b = a.find("h")
c = a.rfind("h")
print(a[:b + 1] + a[c - 1: b:-1] + a[c:])
