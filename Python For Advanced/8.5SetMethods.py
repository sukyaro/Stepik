
# Part 1
# Question 1
# Counts distinct lowercase characters in each input line.
for i in range(int(input())):
    print(len(set(input().lower())))


# Question 2
# Counts distinct lowercase characters across all input lines combined.
string = ""
for i in range(int(input())):
    string += input().lower()
print(len(set(string)))


# Question 3
# Counts distinct words ignoring punctuation marks.
data, data_1 = set((input().lower()).split()), set()
symbols = [".", ",", ";", ":", "-", "?", "!"]
for i in data:
    for j in symbols:
        if j in i:
            k = i.replace(j, "")
            data_1.add(k)
            break
        else:
            k = i
    data_1.add(k)
print(len(data_1))


# Question 4
# Checks for repeated integers in input and prints "YES"/"NO" accordingly.
data, new_set = [int(i) for i in input().split()], set()
for i in data:
    if i in new_set:
        print("YES")
    else:
        print("NO")
        new_set.add(i)


# Question 5
# Calculates percentage of correct answers and prints related info.
def calculate_percentage(number_of_correct, number_of_tries, data):
    if number_of_tries == 0:
        return "You can be the first one who solves this task"
    else:
        percent = 100 / number_of_tries
        correct_percentage = str(number_of_correct * percent)
        floating_point = correct_percentage.find(".")
        if float(correct_percentage) == 0:
            return "You can be the first one who solves this task"
        elif int(correct_percentage[floating_point + 1]) < 5:
            print(f"{len(data)} Solved it right")
            return f"Out of all the tries {correct_percentage[:floating_point]}% are right"
        else:
            print(f"{len(data)} solved it right")
            return f"Out of all the tries {int(correct_percentage[:floating_point]) + 1}% are right"
    
number_of_tries = int(input())
number_of_correct, data = 0, set()
for i in range(number_of_tries):
    new_data = input().split(":")
    if new_data[1] == " Correct":
        number_of_correct += 1
        if new_data[0] not in data:
            data.add(new_data[0])
print(calculate_percentage(number_of_correct, number_of_tries, data))


# Part 2
# Question 1
# Prints number of common elements between two input sets.
print(len(set(input().split()) & set(input().split())))


# Question 2
# Prints sorted intersection of two input sets.
set_1, set_2 = set([int(i) for i in input().split()]), set([int(i) for i in input().split()])
print(*sorted(set_1 & set_2))


# Question 3
# Prints sorted elements in the first set but not in the second.
set_1, set_2 = set([int(i) for i in input().split()]), set([int(i) for i in input().split()])
print(*sorted(set_1 - set_2))


# Question 4
# Prints sorted intersection of multiple sets.
n, myset = int(input()), set([int(i) for i in input()])
for i in range(n - 1):
    myset.intersection_update(set([int(i) for i in input()]))
print(*sorted(myset))


# Part 3
# Question 1
# Checks if two sets are disjoint (no common elements).
set_1 = set([int(i) for i in input()])
set_2 = set([int(i) for i in input()])
if set_1.isdisjoint(set_2):
    print("NO")
else:
    print("YES")


# Question 2
# Checks if the first set is a superset of the second.
set_1 = set([int(i) for i in input()])
set_2 = set([int(i) for i in input()])
if set_1.issuperset(set_2):
    print("YES")
else:
    print("NO")


# Question 3
# Prints sorted elements present in first two sets but not in the third, in reverse order.
set_1 = set([int(i) for i in input().split()])
set_2 = set([int(i) for i in input().split()])
set_3 = set([int(i) for i in input().split()])
print(*sorted(set_1 & set_2 - set_3, reverse=True))


# Question 4
# Prints elements that appear in exactly two of the three sets.
set_1 = set([int(i) for i in input().split()])
set_2 = set([int(i) for i in input().split()])
set_3 = set([int(i) for i in input().split()])
set_4 = set_1 & set_2 ^ set_3 | set_1 & set_3 ^ set_2 | set_2 & set_3 ^ set_1
print(*sorted(set_4))


# Question 5
# Prints elements in third set but not in the union of the first two, in reverse order.
set_1 = set([int(i) for i in input().split()])
set_2 = set([int(i) for i in input().split()])
set_3 = set([int(i) for i in input().split()])
set_4 = set_3.difference(set_1 | set_2)
print(*sorted(set_4, reverse=True))


# Question 6
# Prints elements from 0 to 10 not in any of the three input sets.
set_1 = set([int(i) for i in input().split()])
set_2 = set([int(i) for i in input().split()])
set_3 = set([int(i) for i in input().split()])
set_4 = set(range(11))
print(*sorted(set_4.difference(set_1 | set_2 | set_3)))