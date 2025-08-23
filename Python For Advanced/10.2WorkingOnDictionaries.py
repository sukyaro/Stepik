# Question 1
# Finds the sum of the smallest and largest keys in the dictionary.
my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}
print(min(my_dict) + max(my_dict))


# Question 2
# Prints names of users whose phone numbers end with 8 in alphabetical order.
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

users_sorted = [i["name"] for i in users if i["phone"][-1] == "8"]
print(*sorted(users_sorted))


# Question 3
# Prints names of users with missing or empty email addresses in alphabetical order.
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

print(*sorted([i["name"] for i in users if "email" not in i or i["email"] == ""]))


# Question 4
# Converts digits of a number to words.
digits = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
          5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

normal_number = [int(x) for x in input()]
print(*[digits[d] for d in normal_number])


# Question 5
# Prints full details of a specific course from the list of dictionaries.
CS_details = [{"name": "CS101", "room": 3004, "leacturer": "Hines", "time": "8:00"},
              {"name": "CS102", "room": 4501, "leacturer": "Alevardo", "time": "9:00"},
              {"name": "CS103", "room": 6755, "leacturer": "Rich", "time": "10:00"},
              {"name": "NT110", "room": 1244, "leacturer": "Berk", "time": "11:00"},
              {"name": "CM241", "room": 1411, "leacturer": "Li", "time": "13:00"}]

get_details = input()
for i in CS_details:
    if i["name"] == get_details:
        print(f"{i['name']}: {i['room']}, {i['leacturer']}, {i['time']}")


# Question 6
# Converts a text message into the old-style phone keypad number sequence.
d = {"1": [".", ",", "?", "!", ":"],
     "2": ["A", "B", "C"],
     "3": ["D", "E", "F"],
     "4": ["G", "H", "I"],
     "5": ["J", "K", "L"],
     "6": ["M", "N", "O"],
     "7": ["P", "Q", "R", "S"],
     "8": ["T", "U", "V"],
     "9": ["W", "X", "Y", "Z"],
     "0": [" "]}

message = [i for i in input().upper()]
code = []

for char in message:
    for key, value in d.items():
        if char in value:
            code.append(key * (value.index(char) + 1))

print(*code, sep="")


# Question 7
# Converts a message into Morse code.
morze = {'A':'.-', 'B':'-...', 'C':'-.-.',
         'D':'-..', 'E':'.', 'F':'..-.',
         'G':'--.', 'H':'....', 'I':'..',
         'J':'.---', 'K':'-.-', 'L':'.-..',
         'M':'--', 'N':'-.', 'O':'---',
         'P':'.--.', 'Q':'--.-', 'R':'.-.',
         'S':'...', 'T':'-', 'U':'..-',
         'V':'...-', 'W':'.--', 'X':'-..-',
         'Y':'-.--', 'Z':'--..', '0':'-----',
         '1':'.----', '2':'..---', '3':'...--',
         '4':'....-', '5':'.....', '6':'-....',
         '7':'--...', '8':'---..', '9':'----.'}

message = [i for i in input().upper()]
cypher = [morze[i] for i in message]
print(*cypher, sep=" ")
