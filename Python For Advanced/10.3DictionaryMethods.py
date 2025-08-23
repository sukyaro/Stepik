
# Question 1
# Create a dictionary of squares from 1 to 15
result = {i: i ** 2 for i in range(1, 16)}


# Question 2
# Merge two dictionaries, adding values for keys that exist in both
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

# Add values of overlapping keys
for k in dict1:
    if k in dict2:
        dict1[k] += dict2[k]

# Combine into result
result = dict2.copy()
result.update(dict1)


# Question 3
# Count frequency of each character in a string
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = {}
for char in text:
    result[char] = result.get(char, 0) + 1


# Question 4
# Find the most frequent fruit (alphabetically smallest if tie)
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'.split()
counter = {}
for fruit in s:
    counter[fruit] = counter.get(fruit, 0) + 1

max_count = max(counter.values())
max_values = [k for k, v in counter.items() if v == max_count]

print(min(max_values))  # alphabetically first among most frequent


# Question 5
# Group pets by last name tuple (excluding first name)
pets = [('Hatiko', 'Parker', 'Wilson', 50), 
        ('Rusty', 'Josh', 'King', 25), 
        ('Fido', 'John', 'Smith', 28), 
        ('Butch', 'Jake', 'Smirnoff', 18), 
        ('Odi', 'Emma', 'Wright', 18), 
        ('Balto', 'Josh', 'King', 25), 
        ('Barry', 'Josh', 'King', 25), 
        ('Snape', 'Hannah', 'Taylor', 40), 
        ('Horry', 'Martha', 'Robinson', 73), 
        ('Giro', 'Alex', 'Martinez', 65), 
        ('Zooma', 'Simon', 'Nevel', 32), 
        ('Lassie', 'Josh', 'King', 25), 
        ('Chase', 'Martha', 'Robinson', 73), 
        ('Ace', 'Martha', 'Williams', 38), 
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}
for pet in pets:
    key = pet[1:]  # tuple of (owner_first, owner_last, age)
    result.setdefault(key, []).append(pet[0])


# Question 6
# Find the least frequent word (alphabetically first if tie)
data = input().lower().split()
data_dict = {}
for word in data:
    if word[-1] in ".,!?:;-":  # remove punctuation
        word = word[:-1]
    data_dict[word] = data_dict.get(word, 0) + 1

min_count = min(data_dict.values())
min_values = [k for k, v in data_dict.items() if v == min_count]

print(min(min_values))


# Question 7
# Rename duplicates in a list with suffix "_n"
data = input().split()
dict_data = {}
data_2 = []

for word in data:
    dict_data[word] = dict_data.get(word, 0) + 1
    if dict_data[word] > 1:
        data_2.append(f"{word}_{dict_data[word]-1}")
    else:
        data_2.append(word)

print(*data_2)
