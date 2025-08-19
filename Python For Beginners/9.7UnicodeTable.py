
# Question 1
# Prints all characters from the ASCII value of 'a' to 'b' (inclusive) separated by spaces
a = int(input())
b = int(input())
for i in range((b + 1) - a):
    print(chr(a + i), end=" ")

# Question 2
# Prints the ASCII values of each character in the input string separated by spaces
a = input()
for word in a:
    for letter in word:
        print(ord(letter), end=" ")

# Question 3
# Decrypts a string by shifting letters back by 'a' positions, wrapping around if needed
a = int(input())
b = input()

for letter in b:
    if ord(letter) - a < 97:
        c = ord(letter) - 96
        print(chr(122 - (a - c)), end="")
    else:
        print(chr(ord(letter) - a), end="")
