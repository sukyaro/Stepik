
import math

# Question 1
# Find the tuple with the minimum and maximum arithmetic mean from a list of tuples
numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
def arithmetic_mean(point):
    return sum(point) / len(point)

print(min(numbers, key=arithmetic_mean))
print(max(numbers, key=arithmetic_mean))

# Question 2
# Sort points by distance from origin
points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
def length_from_origin(point):
    x = point[0]
    y = point[1]
    return math.sqrt(x ** 2 + y ** 2)

points.sort(key=length_from_origin)
print(points)

# Question 3
# Sort tuples by sum of their minimum and maximum elements
numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
def min_max_sum(point):
    minimal = min(point)
    maximal = max(point)
    return minimal + maximal

numbers.sort(key=min_max_sum)
print(numbers)

# Question 4
# Sort athletes by chosen attribute (name, age, height, or weight)
athletes = [('Dima', 10, 130, 35), ('Timur', 11, 135, 39), ('Mike', 9, 140, 33), ('Rick', 10, 128, 30), ('Adam', 16, 170, 70), ('Alex', 16, 188, 100), ('Mathew', 17, 168, 68), ('Patrick', 15, 190, 90)]
def sort_by_name(tuple):
    return tuple[0]

def sort_by_age(tuple):
    return tuple[1]

def sort_by_height(tuple):
    return tuple[2]

def sort_by_weight(tuple):
    return tuple[3]

choice = int(input())
choosing_sort = {1 : sort_by_name,
                2 : sort_by_age,
                3 : sort_by_height,
                4 : sort_by_weight}

athletes.sort(key=choosing_sort[choice])
for i in athletes:
   print(*i)

# Question 5
# Apply a chosen mathematical function to a number
def square(number):
    return number ** 2

def cube(number):
    return number ** 3

def root(number):
    return math.sqrt(number)

def module(number):
    return abs(number)

def sin(number):
    return math.sin(number)

num = int(input())
function_choice = input()
function_choices = {"square" : square,
                   "cube"     : cube,
                   "root"  : root,
                   "module"  : module,
                   "sin"   : sin}

print(function_choices[function_choice](num))

# Question 6
# Sort a list of numbers by the sum of their digits
def digit_sum(number):
    sum = 0
    string_number = str(number)
    for i in string_number:
        sum += int(i)
    return sum

num = [int(i) for i in input().split()]
num.sort()
num.sort(key=digit_sum)
print(*num)
