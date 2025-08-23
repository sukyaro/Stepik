
from random import *

# Question 1
# Simulate coin tosses and print "Head" or "Tail"
tries = int(input())
for i in range(tries):
    choice = randint(0, 1)
    if choice == 1:
        print("Head")
    else:
        print("Tail")

# Question 2
# Simulate dice rolls and print numbers from 1 to 6
tries = int(input())
for i in range(tries):
    print(randrange(1, 7))

# Question 3
# Generate a random password of given length with letters and digits
lenght = int(input())
password = []

for i in range(lenght):
    choice = randint(0,2)
    if choice == 0:
        password.append(chr(randint(65, 90)))
    elif choice == 1:
        password.append(chr(randint(97, 122)))
    else:
        password.append(chr(randint(48, 57)))

print(*password, sep="")

# Question 4
# Generate 7 unique random numbers from 1 to 49 and print them sorted
def number():
    num = randint(1, 49)
    return num

def check_number(number, list_of_numbers):
    if number in list_of_numbers:
        return True
    else:
        return False

list_of_numbers = []
for i in range(7):
    new_number = number()
    while check_number(new_number, list_of_numbers) == True:
        new_number = number()
    list_of_numbers.append(new_number)

print(*sorted(list_of_numbers))
