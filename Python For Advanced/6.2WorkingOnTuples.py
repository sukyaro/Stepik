
# Part 1
# Question 1
# Prints the last element of the tuple.
countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
last = countries[-1]
print(last)


# Question 2
# Prints the first six prime numbers from the tuple.
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71) 
print(primes[:6])


# Question 3
# Prints the tuple elements starting from index 2.
countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[2:])


# Question 4
# Prints all tuple elements except the last three.
countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[:-3])


# Question 5
# Prints tuple elements from index 3 to the third-last element.
countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[3:-2])


# Question 6
# Prints the number of elements in the tuple.
countries = ('Romania', 'Poland', 'Estonia', 'Bulgaria', 'Slovakia', 'Slovenia', 'Hungary')
number = len(countries)
print(number)


# Question 7
# Prints the sum of the minimum and maximum values in the tuple.
numbers = (12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324)
print(min(numbers) + max(numbers))


# Question 8
# Finds the index of "Slovenia" in the tuple.
countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy')
index = countries.index("Slovenia")
print(index)


# Question 9
# Counts the number of occurrences of "Spain" in the tuple.
countries = ('Russia', 'Argentina', 'Spain', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Spain', 'Cameroon')
number = countries.count("Spain")
print(number)


# Question 10
# Creates a new tuple by repeating and concatenating given tuples.
numbers1 = (1, 2, 3)
numbers2 = (6,)
numbers3 = (7, 8, 9, 10, 11, 12, 13)
print(numbers1 * 2 + numbers2 * 9 + numbers3)


# Question 11
# Reads city name and year, stores them as a tuple, and prints it.
city_name = input()
city_year = int(input())
city = (city_name, city_year)
print(city)


# Question 12
# Removes empty tuples from a list of tuples.
tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [i for i in tuples if len(i) > 0]
print(non_empty_tuples)


# Question 13
# Replaces the last element of each tuple with 100.
tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = [tuple(i[:-1]) + (100, ) for i in tuples]
print(new_tuples)



# Part 2
# Question 1
# Computes the product of all numbers in the tuple.
numbers, total = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1), 1
for i in numbers:
    total *= i
print(total)


# Question 2
# Converts a string into a tuple of characters.
data = 'Python for advanced!'
print(tuple(data))


# Question 3
# Prints a tuple containing poet information.
poet_data = ('Wilde', 1854, 'Ireland')
print(poet_data)


# Question 4
# Computes the average of numbers inside each tuple and prints a list of averages.
numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
my_list = []
for i in numbers:
    total, counter = 0, 0
    for j in i:
        total += j
        counter += 1
    my_list.append(total / counter)
print(my_list)


# Question 5
# Computes the vertex coordinates of a parabola given coefficients (a, b, c).
coords = tuple([int(input()) for _ in range(3)])
point = ((-coords[1]) / (2 * coords[0]), (4 * coords[0] * coords[2] - coords[1] ** 2) / (4 * coords[0]))
print(point)


# Question 6
# Reads student names and grades, prints all, then prints only top students (grade 4 or 5).
num_of_students = int(input())
grades = [tuple(input().split()) for _ in range(num_of_students)]
top_grade = tuple([i for i in grades if i[1] == "4" or i[1] == "5"])

for i in grades:
    print(*i)
print()
for i in top_grade:
    print(*i)


# Question 7
# Prints the first n Tribonacci numbers (each number is the sum of the previous three).
n = int(input())
f1, f2, f3 = 1, 1, 1
for i in range(n):
    print(f1, end=" ")
    f1, f2, f3 = f2, f3, f1 + f2 + f3
