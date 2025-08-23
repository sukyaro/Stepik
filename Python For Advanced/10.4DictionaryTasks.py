
# Question 1
# Create a slang dictionary and handle lookups
word_count = int(input())
slang_dict = {}
for _ in range(word_count):
    term = input().split(":")
    slang_dict[term[0].lower()] = term[1][1:]  # Remove leading space after ':'

request_number = int(input())
for _ in range(request_number):
    request = input().lower()
    print(slang_dict.get(request, "Not found"))


# Question 2
# Check if two words are anagrams (same letter counts)
word_1, word_2 = input(), input()
dict_1, dict_2 = {}, {}

for c in word_1:
    dict_1[c] = dict_1.get(c, 0) + 1
for c in word_2:
    dict_2[c] = dict_2.get(c, 0) + 1

print("YES" if dict_1 == dict_2 else "NO")


# Question 3
# Check if two sentences are anagrams ignoring punctuation and spaces
word_1, word_2 = input().lower(), input().lower()
dict_1, dict_2 = {}, {}
for c in word_1:
    if c not in ".,!?:;- ":
        dict_1[c] = dict_1.get(c, 0) + 1
for c in word_2:
    if c not in ".,!?:;- ":
        dict_2[c] = dict_2.get(c, 0) + 1

print("YES" if dict_1 == dict_2 else "NO")


# Question 4
# Create a bidirectional dictionary from pairs of words
n_pairs = int(input())
dict_words = {}
for _ in range(n_pairs):
    a, b = input().split()
    dict_words[a] = b
    dict_words[b] = a

print(dict_words[input()])


# Question 5
# Map country cities to their countries
num_of_countries = int(input())
countries = {}
for _ in range(num_of_countries):
    add_country = input().split()
    country_name = add_country[0]
    for city in add_country[1:]:
        countries[city] = country_name

num_to_find = int(input())
for _ in range(num_to_find):
    print(countries[input()])


# Question 6
# Build a phonebook with multiple people per phone
people_num = int(input())
phone_dict = {}
for _ in range(people_num):
    name, phone = input().lower().split()
    if phone in phone_dict:
        phone_dict[phone] += " " + name
    else:
        phone_dict[phone] = name

search_people = int(input())
for _ in range(search_people):
    search = input().lower()
    print(phone_dict.get(search, "The user is not found"))


# Question 7
# Map encrypted letters based on frequency
encrypted_word = input()
dict_size = int(input())
dict_data = {}
encrypted_dict = {}
word = []

# Count frequency of letters in encrypted word
for ch in encrypted_word:
    encrypted_dict[ch] = encrypted_dict.get(ch, 0) + 1

# Build frequency to letter mapping
for _ in range(dict_size):
    letter, freq = input().split(": ")
    dict_data[int(freq)] = letter

# Decrypt based on frequency
for ch in encrypted_word:
    letter = encrypted_dict[ch]
    word.append(dict_data[letter])

print(*word, sep="")