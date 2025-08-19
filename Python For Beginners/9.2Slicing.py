
# Question 1
# Prints the first 12 characters of the string
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[:12])

# Question 2
# Prints the last 9 characters of the string
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-9:])

# Question 3
# Prints every 7th character of the string
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::7])

# Question 4
# Prints the string in reverse order
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::-1])

# Question 5
# Checks if the input string is a palindrome and prints YES or NO
s = input()
if s[:] == s[::-1]:
    print("YES")
else:
    print("NO")

# Question 6
# Prints various string manipulations: 
# length
# repeated string
# first character
# first 3 chars
# last 3 chars
# reversed
# string without first/last char
s = input()
print(len(s))
print(3 * s)
print(s[0])
print(s[:3])
print(s[-3:])
print(s[::-1])
print(s[1:len(s) - 1])

# Question 7
# Prints different slices of the string: 
# 3rd char
# second-to-last char
# first 5 chars
# all but last 2 chars
# every second char
# every second char starting from index 1
# reversed string
# reversed every second char
s = input()
print(s[2])
print(s[-2:-1])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])

# Question 8
# Rotates the string by half its length; if odd, the middle character goes to the front
s = input()
a = len(s) // 2
if len(s) % 2 == 0:
    s = s[a:] + s[:a]
else:
    s = s[a + 1:] + s[:a + 1]
print(s)
