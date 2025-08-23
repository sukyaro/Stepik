from functools import reduce
from operator import add

# Question 1
# Lambda to check if a number is divisible by 19 or 13
func1 = lambda x : x % 19 == 0 or x % 13 == 0

# Question 2
# Lambda to check if a string starts and ends with 'a' (case-insensitive)
func2 = lambda x : x[0].lower() == 'a' and x[-1].lower() == 'a'

# Question 3
# Lambda to check if a string represents a non-negative number
is_non_negative_num = lambda x : x.replace('.', "").isdigit() and x.count('.') < 2

# Question 4
# Lambda to check if a string represents a number (including negative)
is_num = lambda x : x.count('-') < 2 and x[0] == '-' or is_non_negative_num(x)

# Question 5
# Filters words of length 6 and prints them sorted
words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able', 'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound', 'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday', 'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']
print(*sorted(list(filter(lambda x : len(x) == 6, words))), sep=" ")

# Question 6
# Halves even numbers (conditioned) and filters numbers <47 or even >=47
numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
print(*map(lambda x : x // 2 if x % 2 == 0 else x, filter(lambda x : x < 47 or (x >= 47 and x % 2 == 0), numbers)))

# Question 7
# Sorts data by last letter of city name in reverse and prints population and city
data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
data.sort(key=lambda x : x[-1][-1], reverse=True)
for (population, name) in data:
   print(f"{name}: {population}")

# Question 8
# Sorts list first by length, then alphabetically
data = ['year', 'person', 'time', 'deal', 'life', 'day', 'hand', 'once', 'work', 'word', 'place', 'face', 'friend', 'eye', 'question', 'house', 'side', 'country', 'piece', 'situation', 'head', 'child', 'power', 'end', 'apearence', 'system', 'part', 'city', 'relationship', 'woman', 'money']
data.sort()
data.sort(key=lambda x : len(x))
print(*data)

# Question 9
# Finds the maximum numeric value in a mixed list
mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday', 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
print(max(filter(lambda x : str(x)[0].isdigit(), mixed_list)))

# Question 10
# Sorts a mixed list by string representation
mixed_list = ['a', 'ab', 3, 5, 1, 8, 0, 'c', 'ac', 'aab']
print(*sorted(mixed_list, key=lambda x: str(x)))

# Question 11
# Maps list of integers to 255 minus each element
data = [int(x) for x in input().split()]
print(*list(map(lambda x: 255 - x, data)))

# Question 12
# Evaluates a polynomial at given x using coefficients
def evaluate(coefficients, x):
    degree = sorted([i for i in range(len(coefficients))], reverse=True)
    print(reduce(add, map(lambda y, z: y * x ** z, coefficients, degree), 0))

coef = [int(i) for i in input().split()]
x = int(input())
evaluate(coef, x)

