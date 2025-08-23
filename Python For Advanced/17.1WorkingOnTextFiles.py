
import random
from functools import reduce

# Part 1
# Question 1
# Reads and prints the entire content of a file
name_of_file = input()
file = open(name_of_file, 'r')
file_context = file.read()
print(file_context)
file.close()

# Question 2
# Reads a file and prints the second-to-last line
name_of_file = input()
file = open(name_of_file, 'r')
file_context = file.readlines()
print(file_context[-2])
file.close()

# Question 3
# Reads a file and prints a random line
file = open("lines.txt", 'r')
file_context = file.readlines()
print(file_context[random.randint(0, len(file_context) - 1)])
file.close()

# Question 4
# Reads two numbers from a file and prints their sum
file = open('/Users/sukayarik/Desktop/Python/numbers.txt', 'r')
file_context = [x.strip() for x in file.readlines()]
print(int(file_context[0]) + int(file_context[1]))
file.close()

# Question 5
# Reads numbers from a file and prints their sum
file = open('/Users/sukayarik/Desktop/Python/nums.txt', 'r')
file_context = [int(x.strip()) for x in file.readlines() if (x.strip()).isdigit()]
print(sum(file_context))
file.close()

# Question 6
# Calculates total cost from a file with price and quantity columns
file = open('/Users/sukayarik/Desktop/Python/prices.txt', 'r')
file_context = [x.strip().split('\t') for x in file.readlines()]
shopping_sum = reduce(lambda acc, x: acc + int(x[1]) * int(x[2]), file_context, 0)
print(shopping_sum)
file.close()


# Part 2
# Question 1
# Prints the first line of a file in reverse character order
with open('/StepikTextFiles/text.txt', 'r', encoding='utf-8') as file:
   lineLen = len(file.readline().strip())
   for i in range(lineLen - 1, -1, -1):
       file.seek(i)
       print(file.read(1), end="")

# Question 2
# Prints all lines of a file in reverse order
with open('/StepikTextFiles/data.txt', 'r', encoding='utf-8') as file:
   listOfLines = [x.strip() for x in file.readlines()]
   for i in range(len(listOfLines) - 1, -1, -1):
       print(listOfLines[i])

# Question 3
# Prints all lines with the maximum length from a file
with open('/StepikTextFiles/lines1.txt', 'r', encoding='utf-8') as file:
    maxLength = max([len(x.strip()) for x in file.readlines()])
    file.seek(0)
    print(*[x.strip() for x in file.readlines() if len(x.strip()) == maxLength], sep="\n")

# Question 4
# Prints the sum of numbers on each line in a file
with open('/StepikTextFiles/numbers1.txt', 'r', encoding='utf-8') as file:
    print(*[sum([int(y) for y in x.strip().split()]) for x in file.readlines()], sep='\n')

# Question 5
# Sums all digits found in a file
with open('/StepikTextFiles/nums1.txt', 'r', encoding='utf-8') as file:
   str = "".join(x if x.isdigit() else " " for x in file.read())
   print(sum(map(int, str.split())))

# Question 6
# Counts letters, words, and lines in a file
with open('/StepikTextFiles/file.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    banned = [' ', '.', '\n', '!', ',', '?', '"', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print("Input file contains:")
    print(str(reduce(lambda acc, x: acc + 1 if x not in banned else acc, text, 0)) + " letters")
    print(f"{len(text.split())} words")
    print(str(len(text.split('\n'))) + " lines")

# Question 7
# Generates 3 random full names by combining first and last names from files
with open('/StepikTextFiles/first_names.txt', 'r', encoding='utf-8') as names, \
     open('/StepikTextFiles/last_names.txt', 'r', encoding='utf-8') as surnames:
        nameList = names.readlines()
        surnameList = surnames.readlines()
        for i in range(3):
            print(random.choice(nameList).strip() + " " + random.choice(surnameList).strip())

# Question 8
# Prints countries starting with 'G' and population over 500000
with open('/StepikTextFiles/population.txt', 'r', encoding='utf-8') as file:
    text = [i.strip().split('\t') for i in file.readlines()]
    print(*[i[0] for i in list(filter(lambda x: x[0][0] == 'G' and int(x[1]) > 500000, text))], sep='\n')
    
# Question 9
# Reads a CSV file into a list of dictionaries
def read_csv():
    with open('/StepikTextFiles/data.csv', 'r') as file:
        fullData = [] 
        text = [i.strip().split(',') for i in file.readlines()]
        keys = text[0]
        
        for i in range(1, len(text)):
            data = {}
            for j in range(len(keys)):
                data.setdefault(keys[j], text[i][j])
            fullData.append(data)
    return fullData

read_csv()


# Part 3
# Question 1
# Writes user input to a file
with open("/StepikTextFiles/output.txt", 'w', encoding='utf-8') as file:
    file.write(input())

# Question 2
# Writes 25 random numbers to a file
with open("/StepikTextFiles/random.txt", 'w', encoding='utf-8') as file:
    file.writelines(map(lambda x: str(x) + '\n', [random.randint(111, 777) for _ in range(25)]))

# Question 3
# Reads lines from input file and writes them to output with line numbers
with open("/StepikTextFiles/input.txt", 'r', encoding='utf-8') as input, \
     open("/StepikTextFiles/output.txt", 'w', encoding='utf-8') as output:
        output.writelines(map(lambda x: str(x[0]) + ') ' + x[1], enumerate(input.readlines(), start=1)))

# Question 4
# Increases scores by 5, caps at 100, and writes to new file
with open("/StepikTextFiles/class_scores.txt", 'r', encoding='utf-8') as input, \
     open("/StepikTextFiles/new_scores.txt", 'w', encoding='utf-8') as output:
        output.writelines(map(lambda x: x[0] + " " + str(100 if int(x[1]) + 5 >= 100 else int(x[1]) + 5) + '\n', [x.split() for x in input.readlines()]))

# Question 5
# Writes goat colors appearing more than 7% in the list to output file
with open("/StepikTextFiles/goats.txt", 'r', encoding='utf-8') as input, \
     open("/StepikTextFiles/answer.txt", 'w', encoding='utf-8') as output:
        input.readline()
        colours = {}
        sum = 0
        colour = input.readline().strip()
        while colour != "GOATS":
            colours.setdefault(colour, 0)
            colour = input.readline().strip()

        for i in input.readlines():
            sum += 1
            colours[i.strip()] += 1

        value = sum / 100 * 7
        output.writelines(map(lambda x: str(x[0]) + '\n' if x[1] > value else '', colours.items()))

# Question 6
# Appends content of multiple files into a single output file
with open("/StepikTextFiles/output.txt", 'a', encoding='utf-8') as output:
    filesNumber = int(input())
    fileNames = [input() for _ in range(filesNumber)]

    for i in fileNames:
        with open(i, 'r', encoding='utf-8') as input:
            output.writelines(input.readlines())

# Question 7
# Writes lines where duration between timestamps exceeds 60 minutes
with open("/StepikTextFiles/logfile.txt", 'r', encoding='utf-8') as input, \
     open("/StepikTextFiles/output.txt", 'w', encoding='utf-8') as output:
        output.writelines(map(lambda x: x[0] + "\n" if (int(x[2][0] + x[2][1]) * 60 + int(x[2][3] + x[2][4])) - (int(x[1][0] + x[1][1]) * 60 + int(x[1][3] + x[1][4])) >= 60 else '', [i.strip().split(', ') for i in input.readlines()]))