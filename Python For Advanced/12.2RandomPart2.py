
from random import *
import string

# Question 1
# Generate and print a random IPv4 address
def generare_ip():
    print(f"{randrange(256)}.{randrange(256)}.{randrange(256)}.{randrange(256)}")

generare_ip()

# Question 2
# Generate a random custom index with letters and numbers
def generate_index():
    return f"{chr(randint(65, 90))}{chr(randint(65, 90))}{randint(0, 100)}_{randint(0, 100)}{chr(randint(65, 90))}{chr(randint(65, 90))}"

print(generate_index())

# Question 3
# Shuffle rows of a 4x4 matrix
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

new_matrix = []

for i in matrix:
    shuffle(i)
    new_matrix.append(i)

print(new_matrix)

# Question 4
# Generate 100 unique 7-digit random lottery tickets
def number():
    num = randint(1000000, 9999999)
    return num

def check_number(number, list_of_numbers):
    if number in list_of_numbers:
        return True
    else:
        return False

list_of_tickets = []
for i in range(100):
    new_number = number()
    while check_number(new_number, list_of_tickets) == True:
        new_number = number()
    list_of_tickets.append(new_number)

for i in list_of_tickets:
    print(i)

# Question 5
# Shuffle the letters of an input word
word = [i for i in input()]
shuffle(word)
print(*word, sep="")

# Question 6
# Generate a 5x5 Bingo card with unique random numbers and a free center
def number():
    num = randint(1, 75)
    return num

def check_number(number, list_of_numbers):
    counter = 0
    for row in list_of_numbers:
        if str(number).ljust(3) in row:
            counter += 1
    if counter >= 1:
        return True
    else:
        return False

card = [[] for _ in range(5)]
for row in range(5):
    for i in range(5):
        if row == 2 and i == 2:
            new_number = 0
        else:
            new_number = number()
            while check_number(new_number, card) == True:
                new_number = number()
        card[row].append(str(new_number).ljust(3))

for i in card:
    print(*i)

# Question 7
# Randomly assign Secret Santa names without matching original names
num_of_people = int(input())
names = []
for i in range(num_of_people):
    names.append(input())

generated_names = names.copy()

def check_names(names, generated_names):
    counter = 0
    for i in range(num_of_people):
        if names[i] == generated_names[i]:
            counter += 1

    if counter >= 1:
        return True
    else:
        return False
    
shuffle(generated_names)
while check_names(names, generated_names) == True:
    shuffle(generated_names)

for i in range(num_of_people):
    print(f"{names[i]} - {generated_names[i]}")

# Question 8
# Generate multiple passwords avoiding banned ASCII characters
banished = [108, 73, 49, 111, 79, 91, 92, 93, 94, 95, 96]
passwords = []
num_of_passwords = int(input())
password_length = int(input())

def check_password(password, list_of_banished):
   for i in password:
       if ord(str(i)) in list_of_banished:
           return True

def generate_password(password_length):
   password = []
   for i in range(password_length):
       choose = choice(["Num", "Letter"])
       if choose == "Num":
           password.append(randint(1, 9))
       else:
           password.append(chr(randint(65, 122)))
   return password

for i in range(num_of_passwords):
   new_password = generate_password(password_length)
   while check_password(new_password, banished) == True:
       new_password = generate_password(password_length)
   passwords.append(new_password)
   print(*passwords[i], sep="")

# Enhanced password generation enforcing digit, uppercase, lowercase and banished checks
def password_check(password, banished_list):
    dig_counter, low_counter, cap_counter, banished = 0, 0, 0, 0
    for i in password:
        if ord(str(i)) in banished_list:
            banished += 1
        elif str(i).isdigit():
            dig_counter += 1
        elif i in string.ascii_lowercase:
            low_counter += 1
        elif i in string.ascii_uppercase:
            cap_counter += 1
    
    if dig_counter == 0 or low_counter == 0 or cap_counter == 0 or banished > 0:
        return True
    

def generate_password(length):
    password = []
    for i in range(length):
        choose = choice(["Num", "Letter"])
        if choose == "Num":
            password.append(randint(1, 9))
        else:
            password.append(chr(randint(65, 122)))
    return password


def generate_passwords(count, length):
    passwords = []
    for i in range(count):
        new_password = generate_password(length)
        while password_check(new_password, banished) == True:
            new_password = generate_password(length)
        passwords.append(new_password)
    return passwords
        
banished = [108, 73, 49, 111, 79, 91, 92, 93, 94, 95, 96]
num_of_passowrds = int(input())
password_length = int(input())
passwords = generate_passwords(num_of_passowrds, password_length)
for i in passwords:
    print(*i, sep="")
