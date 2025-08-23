
# Part 1
# Question 1
# Filter each list in the dictionary to only include numbers <= 20
my_dictt = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
my_dict = {i: [j for j in my_dictt[i] if j <= 20] for i in my_dictt}

# Question 2
# Combine usernames and domains into email addresses, then sort alphabetically
emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'], 
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'], 
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'], 
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}

sorted_emails = []
for key, value in emails.items():
    for domen in value:
        sorted_emails.append(f"{domen}@{key}")

print(*sorted(sorted_emails), sep="\n")


# Part 2
# Question 1
# Convert a DNA sequence to RNA sequence using mapping
dna_to_rna = {"G":"C", "C":"G", "T":"A", "A":"U"}
chain = [i for i in input()]
for i in chain:
    print(dna_to_rna[i], end="")

# Question 2
# Count occurrences of each word in a sentence and print cumulative counts
sentance, counter = input().split(), {}
for i in sentance:
    counter[i] = counter.get(i, 0) + 1
    print(counter[i], end=" ")

# Question 3
# Calculate Scrabble score for input word based on letter values
word, sum_cost = [i for i in input()], 0
dict_for_letters = {1:["A", "E", "I", "L", "N", "O", "R", "S", "T", "U"],
                    2: ["D", "G"],
                    3: ["B", "C", "M", "P"],
                    4: ["F", "H", "V", "W", "Y"],
                    5: ["K"],
                    8: ["J", "X"],
                    10: ["Q", "Z"]}

for i in word:
    for key, values in dict_for_letters.items():
        if i in values:
            sum_cost += key

print(sum_cost)

# Question 4
# Build a URL query string from dictionary sorted by keys
def build_query_string(dict):
    data = []
    for i in dict:
        data.append(f"{i}={dict[i]}")
    data = "&".join(sorted(data))
    return data

print(build_query_string({'a': 'b', 'c': 'd', 'stepik': 'beegeek', 'iq': 'option', 'rita': 'ora'}))

# Question 5
# Merge list of dictionaries into one, storing values as sets
def merge(list_of_dicts):
    new_dict = {}
    for dict in list_of_dicts:
        for i in dict:
            new_dict[i] = new_dict.get(i, set()).union({dict[i]}) 
    return new_dict

# Question 6
# Check file access permissions and print whether access is allowed
number_of_files, file_dict = int(input()), {}
for i in range(number_of_files):
    file = input().split()
    file_dict[file[0]] = file[1:]

access_tries = int(input())
for i in range(access_tries):
    access_file = input().split()
    if access_file[0][0].upper() in file_dict[access_file[1]]:
        print("OK")
    elif "X" in file_dict[access_file[1]] and access_file[0] == "execute":
        print("OK")
    else:
        print("Access denied")

# Question 7
# Track customer shopping carts and print sorted items for each customer
number_of_customers, shopping_box = int(input()), {}
for i in range(number_of_customers):
    customer = input().split()
    shopping_box[customer[0]] = shopping_box.setdefault(customer[0], {})
    if customer[0] in shopping_box:
        if customer[1] in shopping_box[customer[0]]:
            shopping_box[customer[0]][customer[1]] += int(customer[2])
        else:
            shopping_box[customer[0]].update({customer[1]: int(customer[2])})
    else:
        shopping_box[customer[0]] = {customer[1]: int(customer[2])}

names = sorted(shopping_box)
for i in names:
    print(f"{i}:")
    items = sorted(shopping_box[i])
    for j in items:
        print(j, shopping_box[i][j])
