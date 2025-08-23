
from functools import reduce 

# Question 1
# Squares each float in the list and rounds the result to 1 decimal place
floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
numbers = [4, 6, 9, 23, 5]

map_result = list(map(lambda num: round(num**2, 1), floats))

# Question 2
# Filters words to keep only palindromes longer than 4 characters
filter_result = list(filter(lambda name: name if name == name[::-1] and len(name) > 4 else None, words))

# Question 3
# Reduces numbers by multiplying all elements together
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)

print(map_result)
print(filter_result)
print(reduce_result)

# Question 4
# Filters primary cities with population over 10 million and sorts them alphabetically
data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]

primary_cities = list(filter(lambda city: city[2] == "primary", data))
primary_cities = list(filter(lambda city: city[1] > 10000000, primary_cities))
primary_cities = [city[0] for city in primary_cities]
primary_cities_sorted = sorted(primary_cities)

print("Cities:", ", ".join(primary_cities_sorted))