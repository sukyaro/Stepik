
# Imports
from functools import reduce

# Question 1
# Given a name of the file, we need to output the number of lines in this file
fileName = input()
with open(fileName, 'r', encoding='utf-8') as file:
    print(len(file.readlines()))

# Question 2
## Given a file where on each line were given how much a customer spent at the shop, we need to calculate
## the total and output it
with open('/StepikTextFiles/ledger.txt', 'r', encoding='utf-8') as file:
    print('$' + str(reduce(lambda acc, x: acc + int(x.lstrip('$')), file.readlines(), 0)))

# Question 3
## Given a file where on each line we have a name of the sturend and the grade they got in each term
## The program should output how many students passed, a pass is a grade above 65
with open('/StepikTextFiles/grades.txt', 'r', encoding='utf-8') as file:
    print(sum(1 for i in file.readlines() if all([int(j) >= 65 for j in i.split(' ')[1::]])))

# Question 4
## Given a file with words we need to ouput the longest words in the file, every word on a separate line
with open('/StepikTextFiles/words.txt', 'r', encoding='utf-8') as file:
    maxLen = len(max(file.read().split(), key=len))
    file.seek(0)
    print(*filter(lambda x: len(x) == maxLen, file.read().split()), sep='\n')

# Question 5
## We are given a file and we need to ouput the last 10 lines of the file
fileName = input()

with open(fileName, 'r') as file:
    print(*[i.strip() for i in file.readlines()[-10:]], sep='\n')

# Question 6
## Given a file of forbidden words and then a file with text, the task is to replace all the forbidden words in that text
## to *, we need to replace it even if the forbidden word is within another word
with open('/StepikTextFiles/forbidden_words.txt', 'r', encoding='utf-8') as words:
    forbWords = words.read().strip().split()
    file = input()
    with open(file, 'r', encoding='utf-8') as file:    
        text = file.read().strip()
        text_lower = text.lower()
        for j in forbWords:
            text_lower = text_lower.replace(j, '*'*len(j))

        test = ""

        for k in range(len(text)):
            if text_lower[k] == '*':
                test += '*'
            elif text_lower[k] != '*' and text_lower[k] != text[k]:
                test += text[k]
            else:
                test += text_lower[k]

    print(test)

# Question 7
## We are given a text written in cyrillic, we need to translate every letter into the English alphabet
## if the letter is in English we dont change it and the we write it all into a new file
translate_dict = {
    'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
    'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
    'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
    'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya',
    'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'Ch',
    'Г': 'G', 'Н': 'N', 'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*',
    'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh', 'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je',
    'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya',
    }

with open('/StepikTextFiles/cyrillic.txt', 'r', encoding='utf-8') as input, \
     open('/StepikTextFiles/transliteration.txt', 'w', encoding='utf-8') as output:
        text = input.readlines()
        for i in text:
            output.writelines(map(lambda x: translate_dict[x] if x in translate_dict else x, i))
             
# Question 8
## Given a Python text with functions, if a function does not have a comment we need to output it, if it does we move on
fileName = input()

with open(fileName, 'r', encoding='utf-8') as file:
    hashTags = 0
    badFunctions = []
    text = [i.strip().split() for i in file.readlines()]
    for i in text:
        if len(i) == 0:
            continue

        if i[0] == '#':
             hashTags += 1

        if i[0] == "def":
            if hashTags == 1:
                hashTags -= 1
            else:
                badFunctions.append(i[1][:i[1].find('(')])
    
    if len(badFunctions) == 0:
        print("Best Programming Team")
    else:
        print(*badFunctions, sep='\n')