# Question 1
# Create a list of even numbers from 2 up to the input number
lis = list(range(2, int(input()) + 1, 2))
print(lis)

# Question 2
# Sum corresponding elements from two lists of numbers
a, b = input().split(), input().split()
c = [int(a[i]) + int(b[i]) for i in range(len(a))]
print(*c)

# Question 3
# Validate a phone number format (XXX-XXX-XXXX or 7-XXX-XXX-XXXX)
a = input().split("-")
Flag = True
Flag_1 = True

if len(a) == 3:
    for i in range(2):
        if len(a[i]) != 3 or not a[i].isdigit():
            Flag = False
    if len(a[2]) != 4 or not a[2].isdigit():
        Flag_1 = False

elif len(a) == 4:
    if a[0] != "7":
        Flag = False
    else:
        for i in range(1, 3):
            if len(a[i]) != 3 or not a[i].isdigit():
                Flag = False
        if len(a[3]) != 4 or not a[3].isdigit():
            Flag_1 = False
else:
    Flag = False

print("YES" if Flag and Flag_1 else "NO")

# Question 4
# Print the length of the longest word from input
big = [len(i) for i in input().split()]
print(max(big))

# Question 5
# Convert words to a Pig Latin style with "lo" suffix
word = [i[1:] + i[0] + "lo" for i in input().split()]
print(*word)
