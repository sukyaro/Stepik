
# Question 1
# Removes the first character from each Python keyword and prints the new list
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [m[1:] for m in keywords]
print(new_keywords)

# Question 2
# Creates a list of the lengths of each keyword and prints it
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
lengths = [len(m) for m in keywords]
print(lengths)

# Question 3
# Prints keywords that have 5 or more characters
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [lol for lol in keywords if len(lol) >= 5]
print(new_keywords)

# Question 4
# Finds and prints all palindromic numbers between 100 and 1000
palindromes = [lol for lol in range(100, 1001) if str(lol) == str(lol)[::-1]]
print(palindromes)

# Question 5
# Creates a list of squares from 1 to input number and prints each on a new line
a = [i ** 2 for i in range(1, int(input()) + 1)]
print(*a, sep="\n")

# Question 6
# Cubes each input number and prints the results
a = input().split()
b = [int(lol) ** 3 for lol in a]
print(*b)

# Question 7
# Prints each input element on a new line
a = input().split()
print(*a, sep="\n")

# Question 8
# Extracts and prints all digits from input
a = input().split()
b = [j for i in a for j in i if j in "0123456789"]
print(*b, sep="")

# Question 9
# Squares even numbers from input whose squares do not end with 4 and prints them
print(*[int(i) ** 2 for i in input().split() if int(i) ** 2 % 10 != 4 and int(i) % 2 == 0])
