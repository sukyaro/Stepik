
# Question 1
# Uses str.format() to insert values into placeholders in the string
s = 'In {0}, someone paid {1} {2} for two pizzas.'
print(s.format(2010, '10k', 'Bitcoin'))

# Question 2
# Uses f-string with str.format() to insert values into the string
s = 'In {}, someone paid {} {} for two pizzas.'
print(f"{s.format(2010, '10k', 'Bitcoin')}")

# Question 3
# Prints a formatted string showing exchange rates for euro and yuan on a given date
date = input()
rublesForEuro = float(input())
rublesForYuan = float(input())
print(f"On the {date} : 1€ = {rublesForEuro}₽, 1¥ = {rublesForYuan}₽")

# Question 4
# Prints the sum of cubes and cube of sum for two input numbers using f-strings
number1 = int(input())
number2 = int(input())
print(f"For the numbers {number1} and {number2}:")
print(f"  The sum of the cubes: {number1}**3 + {number2}**3 = {number1 ** 3 + number2 ** 3}")
print(f"  The cube of the sum: ({number1} + {number2})**3 = {(number1 + number2) ** 3}")
