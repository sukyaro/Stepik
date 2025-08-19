# Question 1
# Combines parts of a string to form a sentence with quotes and an apostrophe
s1 = '"Python is a great language!", said Fred. "I don'
s2 = "'"
s3 = 't ever remember having this much fun before."'

res = s1 + s2 + s3
print(res)

# Question 2
# Prints the length of a given football team name
a = input()
print("The football tesm", a, "has a length of", len(a), "symbols")

# Question 3
# Attempts to find and print the shortest and longest of three input strings based on length
a = input()
b = input()
c = input()
a1 = len(a)
b1 = len(b)
c1 = len(c)
if b1 < a1 < c1 or b1 < c1 < a1:
    print(b) 
elif b1 < a1 < c1 or b1 < c1 < a1:
    print(b)
elif a1 < b1 < c1 or a1 < c1 < b1:
    print(a)
elif c1 < a1 < b1 or c1 < b1 < a1:
    print(c)
if a1 < b1 < c1 or b1 < a1 < c1:
    print(c)
elif a1 < c1 < b1 or c1 < a1 < b1:
    print(b)
elif c1 < b1 < a1 or b1 < c1 < a1:
    print(a)

# Question 4
# Checks if the middle-length string's length is equidistant from the shortest and longest lengths
a = input()
b = input()
c = input()
a1 = len(a)
b1 = len(b)
c1 = len(c)
if (a1 + b1 + c1 - max(a1, b1, c1) - min(a1, b1, c1)) - min(a1, b1, c1) == max(a1, b1, c1) - (a1 + b1 + c1 - max(a1, b1, c1) - min(a1, b1, c1)):
    print("YES")
else:
    print("NO")

# Question 5
# Checks if the word "blue" is present in the input string
a = input()
if "blue" in a:
    print("YES")
else:
    print("NO")

# Question 6
# Checks if the input string contains "saturday" or "sunday"
s = input()
if "saturday" in s:
    print("YES")
elif "sunday" in s:
    print("YES")
else:
    print("NO")

# Question 7
# Checks if the input string contains both "@" and ".", useful for basic email validation
s = input()
if "@" in s and "." in s:
    print("YES")
else:
    print("NO")
