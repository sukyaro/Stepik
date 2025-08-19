
# Question 1
# Creates a list of numbers from 1 to the input number
a = int(input())
b = list(range(1, a + 1))
print(b)

# Question 2
# Prints a list of the first 'a' letters of the English alphabet
a = int(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(list(alphabet[:a]))

# Question 3
# Prints a list of odd numbers from 0 up to the input number
print([i for i in range(int(input()) + 1) if i % 2 != 0])

# Question 4
# Prints the indices of every second character in the input string
myString = input()
for i in range(0, len(myString), 2):
    print(i)

# Question 5
# Creates a list of every second character in the input string
myString = input()
myList = []
for i in range(0, len(myString), 2):
    myList.append(myString[i])
print(myList)
