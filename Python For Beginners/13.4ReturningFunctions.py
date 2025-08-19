
import math

# ================= Part 1 =================
# Question 1: Convert km to miles
def convert_to_miles(km):
    return km * 0.6214

print(convert_to_miles(int(input())))

# Question 2: Get number of days in a month
def get_days(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        return 28
    else:
        return 30

print(get_days(int(input())))

# Question 3: Get all factors of a number
def get_factors(num):
    return [i for i in range(1, num+1) if num % i == 0]

print(get_factors(int(input())))

# Question 4: Count number of factors
def count_factors(num):
    return len(get_factors(num))

print(count_factors(int(input())))

# Question 5: Find all occurrences of a symbol in a string
def find_all(target, symbol):
    return [i for i, ch in enumerate(target) if ch == symbol]

target, symbol = input(), input()
print(find_all(target, symbol))

# Question 6: Merge two lists, convert to int, and sort
def merge(list1, list2):
    return sorted([int(x) for x in list1 + list2])

list1, list2 = input().split(), input().split()
print(merge(list1, list2))

# Question 7: Merge multiple sorted lists
def quick_merge(list1, list2):
    result = []
    p1 = p2 = 0
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1
    result += list1[p1:] + list2[p2:]
    return result

merged_list = []
for _ in range(int(input())):
    temp_list = list(map(int, input().split()))
    merged_list = quick_merge(merged_list, temp_list)
print(*merged_list)

# ================= Part 2 =================
# Question 1: Check triangle validity
def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

print(is_valid_triangle(int(input()), int(input()), int(input())))

# Question 2: Check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

print(is_prime(int(input())))

# Question 3: Find next prime number
def next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num

print(next_prime(int(input())))

# Question 4: Check password strength
def is_password_good(pas):
    return (
        len(pas) >= 8 and
        any(c.isupper() for c in pas) and
        any(c.islower() for c in pas) and
        any(c.isdigit() for c in pas)
    )

print(is_password_good(input()))

# Question 5: Check if strings differ by one character
def is_one_away(one, two):
    if len(one) != len(two):
        return False
    return sum(one[i] != two[i] for i in range(len(one))) == 1

print(is_one_away(input(), input()))

# Question 6: Check if a text is a palindrome (ignoring punctuation and case)
def is_palindrome(text):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome(input()))

# Question 8: Check correct bracket sequence
def is_correct_bracket(text):
    stack = 0
    for ch in text:
        if ch == "(":
            stack += 1
        elif ch == ")":
            stack -= 1
            if stack < 0:
                return False
    return stack == 0

print(is_correct_bracket(input()))

# Question 9: Convert CamelCase to python_case
def convert_to_python_case(text):
    result = text[0].lower()
    for c in text[1:]:
        if c.isupper() and not c.isdigit():
            result += "_" + c.lower()
        else:
            result += c.lower()
    print(result)

convert_to_python_case(input())

# ================= Part 3 =================
# Question 1: Get middle point
def get_middle(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2

x, y = get_middle(int(input()), int(input()), int(input()), int(input()))
print(x, y)

# Question 2: Circle data
def circle_data(r):
    return 2 * math.pi * r, math.pi * r ** 2

c, s = circle_data(float(input()))
print(c, s)

# Question 3: Solve quadratic equation
def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return min(x1, x2), max(x1, x2)

x1, x2 = solve(int(input()), int(input()), int(input()))
print(x1, x2)
