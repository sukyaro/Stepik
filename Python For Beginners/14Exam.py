
import math

# Question 1: Draw a centered triangle
def draw_triangle():
    for i in range(8):
        print(" " * (7 - i) + "*" * (1 + i * 2))

draw_triangle()


# Question 2: Compute shipping cost
def get_shipping_cost(quantity):
    if quantity <= 0:
        return 0
    cost = 1000 + (quantity - 1) * 120
    print(cost)

get_shipping_cost(int(input()))


# Question 3: Compute binomial coefficient C(n, k)
def compute_binom(n, k):
    return math.comb(n, k)  # math.comb is available in Python 3.8+

print(compute_binom(int(input()), int(input())))


# Question 4: Get month name in Russian or English
names_en = ["january", "february", "march", "april", "may", "june",
            "july", "august", "september", "october", "november", "december"]
names_ru = ["январь", "февраль", "март", "апрель", "май", "июнь",
            "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

def get_month(lang, num):
    if lang == "ru":
        return names_ru[num - 1]
    else:
        return names_en[num - 1]

print(get_month(input(), int(input())))


# Question 5: Check if date is "magic" (dd.mm.yy)
def is_magic(date):
    day, month, year = map(int, date.split("."))
    return day * month == year

print(is_magic(input()))


# Question 6: Check if text is a pangram
import string

def is_pangram(text):
    text = text.lower()
    return all(c in text for c in string.ascii_lowercase)

print(is_pangram(input()))
