from functools import reduce
from operator import add

# Question 1
# Checks if a command contains any forbidden keywords
def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    
    return any(map(lambda x : x in command, ignore))

print(ignore_command('get ip'))
print(ignore_command('select all'))
print(ignore_command('delete'))
print(ignore_command('trancate'))

# Question 2
# Prints countries with their capitals and populations
countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

for country, capital, number in zip(countries, capitals, population):
   print(f"{capital} is the capital of {country}, population equal {number} people.")

# Question 3
# Checks if points lie inside or on the surface of a sphere of radius 2
abscissas = [float(i) for i in input().split()]
ordinates = [float(i) for i in input().split()]
applicates = [float(i) for i in input().split()] 
true_false = []

for point in zip(abscissas, ordinates, applicates):
   element = (reduce(add, map(lambda x: x ** 2, point), 0.0))
   true_false.append(element <= 4.0)

print(all(true_false))
print(all(x**2 + y**2 + z**2 <= 4 for x, y, z in zip(abscissas, ordinates, applicates)))

# Question 4
# Checks if an input string is a valid IPv4 address
ip_address = [i for i in input().split('.')]
print(all(i.isdigit() and 0 <= int(i) <= 255 for i in ip_address))

# Question 5
# Finds numbers in a range divisible by all their non-zero digits
number1 = int(input())
number2 = int(input())
my_list = [i for i in range(number1, number2 + 1) if '0' not in str(i)]
end_list = []

for i in my_list:
   if all(i % int(y) == 0 for y in str(i)):
       end_list.append(i)

print(*end_list)

# Question 6
# Checks if a password meets requirements: upper, lower, digit, length >=7
password = input()
is_good = all([any(x in 'QWERTYUIOPASDFGHJKLZXCVBNM' for x in password), 
               any(x in 'qwertyuiopasdfghjklzxcvbnm' for x in password), 
               any(x in '123456789' for x in password),
               len(password) >= 7])

if is_good:
   print("YES")
else:
   print("NO")


# Question 7
# Checks if every class has at least one student with grade 5
class_number = int(input())
true_false = []
for i in range(class_number):
    students = int(input())
    grades = [input().split() for _ in range(students)]
    is_a_star = any(int(i[1]) == 5 for i in grades)
    true_false.append(is_a_star)
    
if all(true_false):
    print("YES")
else:
    print("NO")