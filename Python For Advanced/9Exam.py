# Part 1
# Question 1
# Prints elements in set1 that are not in set2.
set1 = {"p"}
set2 = {'a', 't', 'f'}

print(set1 - set2)


# Part 2
# Question 1
# Calculates how many items are unique to the first input compared to the sum of other three inputs.
print(int(input()) - (int(input()) + int(input()) - int(input())))


# Question 2
# Counts how many duplicates are in a list of integers.
list_of_data = [int(x) for x in input().split()]
set_of_data = set(list_of_data)
print(len(list_of_data) - len(set_of_data))


# Question 3
# Checks if a newly entered city name is already in the set of cities.
set_of_cities = set()
for i in range(int(input())):
    set_of_cities.add(input())

old_len_of_set = len(set_of_cities)
set_of_cities.add(input())
if len(set_of_cities) == old_len_of_set:
    print("REPEAT")
else:
    print("OK")


# Question 4
# Checks for each book to read whether it is already on the computer.
books_on_computer, books = set(), []
num_books_on_comp, num_books_to_read = int(input()), int(input())
for i in range(num_books_on_comp):
    books_on_computer.add(input())
for i in range(num_books_to_read):
    if input() in books_on_computer:
        books.append("YES")
    else:
        books.append("NO")

for i in books:
    print(i)


# Question 5
# Prints the intersection of two sets in descending order or "BAD DAY" if there is no intersection.
num_1= set([int(i) for i in input().split()])
num_2 = set([int(i) for i in input().split()])
if len(num_1 & num_2) > 0:
    print(*sorted(num_1 & num_2, reverse=True))
else:
    print("BAD DAY")


# Question 6
# Checks if two sets are equal.
num_1= set([int(i) for i in input().split()])
num_2 = set([int(i) for i in input().split()])
if num_1 == num_2:
    print("YES")
else:
    print("NO")


# Question 7
# Counts math students who are not in CS students.
math_stud, cs_stud = int(input()), int(input())
math_stud_names, cs_stud_names = set(), set()
for i in range(math_stud):
    math_stud_names.add(input())
for i in range(cs_stud):
    cs_stud_names.add(input())

print(len(math_stud_names.difference(cs_stud_names)))


# Question 8
# Prints the size of symmetric difference between math and CS students or "NO" if none.
math_stud, cs_stud = int(input()), int(input())
math_stud_names, cs_stud_names = set(), set()
for i in range(math_stud):
    math_stud_names.add(input())
for i in range(cs_stud):
    cs_stud_names.add(input())

if len(math_stud_names.symmetric_difference(cs_stud_names)) == 0:
    print("NO")
else:
    print(len(math_stud_names.symmetric_difference(cs_stud_names)))


# Question 9
# Prints the union of two employee sets in sorted order.
emp_1, emp_2 = set([i for i in input().split()]), set([i for i in input().split()])
print(*sorted(emp_1 | emp_2))


# Question 10
# Counts students enrolled only in one of two groups.
students = int(input()) + int(input())
math_stud_names, cs_stud_names = set(), set()
for i in range(students):
    new_stud = input()
    if new_stud in math_stud_names:
        cs_stud_names.add(new_stud)
    else:
        math_stud_names.add(new_stud)

if len(math_stud_names.symmetric_difference(cs_stud_names)) == 0:
    print("NO")
else:
    print(len(math_stud_names.symmetric_difference(cs_stud_names)))


# Question 11
# Finds the intersection of multiple sets of lessons.
num_of_lessons = int(input())
main_set = set([input() for _ in range(int(input()))])
for i in range(num_of_lessons - 1):
    new_set = set()
    for j in range(int(input())):
        new_set.add(input())
    main_set.intersection_update(new_set)

main_set = sorted(main_set)
print()
for i in main_set:
    print(i)
