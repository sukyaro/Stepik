from functools import reduce
from operator import *

# 16.1 Part1 15/16
# Generates a formatted email with exam details and optional teacher/classroom
def generate_letter(mail, name, date, time, place, teacher="Тимур Гуев", number=17):
    email = f"""To: {mail}
Hello, {name}!
You have got an exam on the {date}, at {time}.
The address is {place}.
Your examiner is {teacher} in the classroom {number}.
Good luck!"""
    return email

print(generate_letter('lara@yandex.ru', 'Lucy', '10 december', '12:00pm', 'Lime Street, block 2'))
print()
print(generate_letter('lara@yandex.ru', 'Lucy', '10 december', '12:00pm', 
                     'Lime Street, block 2', 'Professor Patel', 23))


# 16.1 Part1 16/16
# Prints a list neatly with borders and optional side character or delimiter
def pretty_print(data, side='-', delimiter='|'):
    string = delimiter
    for i in data:
        string += " " + str(i) + " " + delimiter
    print(" " + (len(string) - 2) * side + " ")
    print(string)
    print(" " + (len(string) - 2) * side + " ")
    
pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')


# 16.3 Part3 1/11
# Concatenates all arguments into a string with an optional separator
def concat(*data, sep=" "):
    string = sep.join(map(str, data))
    return string

print(concat('hello', 'python', 'and', 'stepik'))
print(concat('hello', 'python', 'and', 'stepik', sep='*'))
print(concat('hello', 'python', sep='()()()'))
print(concat('hello', sep='()'))
print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))


# 16.3 Part3 2/11
# Returns the product of all odd numbers in a list
def product_of_odds(data):
    return reduce(mul, filter(lambda x : x % 2 != 0, data), 1)

print(product_of_odds(list(range(1, 10))))


# 16.3 Part3 3/11
# Wraps each word in single quotes
words = 'the world is mine take a look what you have started'.split()
print(*map(lambda x : "'" + x + "'", words))


# 16.3 Part3 4/11
# Filters numbers that are not palindromes
numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
print(*filter(lambda x : str(x) != str(x)[::-1], numbers))


# 16.3 Part3 5/11
# Sorts tuples based on their arithmetic mean in descending order
numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
sorted_numbers = sorted(numbers, key=lambda x : sum(x) / len(x), reverse=True)
print(sorted_numbers)


# 16.3 Part3 6/11
# Calls a function with arbitrary arguments
def call(func, *args):
    return func(*args)

def mul7(x):
    return x * 7

def add2(x, y):
    return x + y

def add3(x, y, z):
    return x + y + z

print(call(mul7, 10))
print(call(add2, 2, 7))
print(call(add3, 10, 30, 40))
print(call(bool, 0))


# 16.3 Part3 7/11
# Composes two functions into a single callable
def compose(f, g):
    return lambda x: f(g(x))

def add3(x):
    return x + 3

def mul7(x):
    return x * 7

print(compose(mul7, add3)(1))
print(compose(add3, mul7)(2))
print(compose(mul7, str)(3))
print(compose(str, mul7)(5))


# 16.3 Part3 8/11
# Returns a function corresponding to a basic arithmetic operation
def arithmetic_operation(operation):
    operations = {'+': add,
                  '-': sub,
                  '*': mul, 
                  '/': truediv}
    
    return operations[operation]

add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))


# 16.3 Part3 9/11
# Sorts a list of strings case-insensitively
def smart_sort(line):
    return sorted(line, key=lambda x: x.lower())

print(*smart_sort(input().split()))


# 16.3 Part3 10/11
# Sorts words based on their "gematria" value (sum of letter positions)
def word_gematry(words):
    words_gematry = []
    for word in words:
        words_gematry.append((word, (reduce(lambda acc, x: acc + (ord(x) - ord('A')), word.upper(), 0))))
    
    words_gematry.sort(key=lambda x: x[1])
    
    return words_gematry

words = []
num_of_words = int(input())
for _ in range(num_of_words):
   words.append(input())
words.sort()

sorted_words = word_gematry(words)
print(*(sorted_words[x][0] for x in range(len(sorted_words))), sep='\n')

# Alternative version 
# def gem(word): 
#   return sum(map(lambda c: ord(c.upper()) - ord('A'), word)), word 
#   words = [input() for _ in range(int(input()))] 
#   print(*sorted(words, key=gem), sep='\n')


# 16.3 Part3 11/11
# Converts IP addresses to integers and sorts them numerically
def func(ip_address):
    degrees = [3, 2, 1, 0]
    return sum(map(lambda x, y: int(x) * 256 ** y, ip_address, degrees))

ip_addresses = [input().split(".") for i in range(int(input()))]

for i in sorted(ip_addresses, key=func):
    print(".".join(i))
