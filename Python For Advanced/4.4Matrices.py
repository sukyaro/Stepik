# Part 1
# Question 1
# Reads dimensions and fills a matrix with user input, then prints it row by row.
down, lengh= int(input()), int(input())
mat = [["a"] * lengh for _ in range(down)]

for i in range(down):
    for j in range(lengh):
        mat[i][j] = input()

for i in range(down):
    for j in range(lengh):
        print(mat[i][j], end=" ")
    print()

# Question 2
# Reads a matrix and prints it, then prints its transpose.
down, lengh= int(input()), int(input())
mat = [["a"] * lengh for _ in range(down)]

for i in range(down):
    for j in range(lengh):
        mat[i][j] = input()

for i in range(down):
    for j in range(lengh):
        print(mat[i][j], end=" ")
    print()
print()

for i in range(lengh):
    for j in range(down):
        print(mat[j][i], end=" ")
    print()

# Question 3
# Calculates the sum of main diagonal elements of a square matrix.
size, suum, num = int(input()), 0, 0
for i in range(size):
    suum += int(input().split()[num])
    num += 1

print(suum)

# Question 4
# Counts how many elements in each row are greater than the row's average.
size, num = int(input()), []
for i in range(size):
    suum = 0
    mat = [int(x) for x in input().split()]
    avg = sum(mat) / size
    for j in range(size):
        if mat[j] > avg:
            suum += 1
    num.append(suum)

print(*[x for x in num], sep="\n")

# Question 5
# Finds the maximum element in the lower-left triangle of a matrix (including diagonal).
size, num, num_1 = int(input()), -10000, 0
for i in range(size):
    mat = [int(x) for x in input().split()]
    for j in range(num_1 + 1):
        if mat[j] > num:
            num = mat[j]
    num_1 += 1

print(num)

# Question 6
# Finds the maximum element inside the main diagonals (both diagonals and central diamond).
size, num, num_1 = int(input()), -10000, 0
for i in range(size):
    mat = [int(x) for x in input().split()]
    for j in range(size):
        if j == size - i - 1 or i == j:
             if mat[j] > num:
                num = mat[j]           
        if i > j and i < size - 1 - j:
            if mat[j] > num:
                num = mat[j]
        if i < j and i > size - 1 - j:
            if mat[j] > num:
                num = mat[j]

print(num)

# Question 7
# Calculates sums of elements in four triangular quarters of a square matrix.
size, sum_left, sum_right, sum_up, sum_down  = int(input()), 0, 0, 0, 0
for i in range(size):
    mat = [int(x) for x in input().split()]
    for j in range(size):          
        if i > j and i < size - 1 - j:
            sum_left += mat[j]
        if i > j and i > size - 1 - j:
            sum_up += mat[j]
        if i < j and i > size - 1 - j:
            sum_right += mat[j]
        if i < j and i < size - 1 - j:
            sum_down += mat[j]

print(f"Upper quater: {sum_down}")
print(f"Right quater: {sum_right}")
print(f"Lower quater: {sum_up}")
print(f"Left quater: {sum_left}")


# Part 2
# Question 1
# Prints multiplication table of given dimensions.
down, lenght = int(input()), int(input())
[print(*[i * j for j in range(lenght)]) for i in range(down)]

# Question 2
# Finds the maximum element in a matrix and prints its coordinates.
down, lenght, maxx, save = int(input()), int(input()), -1000, []
for i in range(down):
    mat = [int(x) for x in input().split()]
    for j in range(lenght):
        if mat[j] > maxx:
            maxx = mat[j]
            save = i, j

print(*save)

# Question 3
# Swaps two specified columns in a matrix.
down, lenght = int(input()), int(input())
mat = [[int(x) for x in input().split()] for _ in range(down)]
change = input().split()
for i in range(down):
    temp, temp_1 = mat[i][int(change[0])], mat[i][int(change[1])]
    mat[i][int(change[1])] = temp
    mat[i][int(change[0])] = temp_1

for i in range(down):
    for j in range(lenght):
        print(mat[i][j], end=" ")
    print()

# Question 4
# Checks if a matrix is symmetric relative to its main diagonal.
size, summ = int(input()), 0
mat, mat_1 = [[int(i) for i in input().split()] for _ in range(size)], []
for i in range(size):
    a = []
    for j in range(size):
        a += [mat[j][i]]
    mat_1.extend([a])

if mat == mat_1:
    print("YES")
else:
    print("NO")

# Question 5
# Swaps the main diagonal and the secondary diagonal of a square matrix.
size, temp, temp_1 = int(input()), [], []
mat = [[int(i) for i in input().split()] for _ in range(size)]

for i in range(size):
    temp.append(mat[i][i])
    temp_1.append(mat[i][size - i - 1])

for i in range(size):
    mat[i][i] = temp_1[-1 - i]
    mat[i][size - i - 1] = temp[-1 - i]

for i in range(size):
    for j in range(size):
        print(mat[i][j], end=" ")
    print()

# Question 6
# Rotates a square matrix 90 degrees clockwise.
size = int(input())
mat, mat_1 = [[int(i) for i in input().split()] for _ in range(size)], [[] for _ in range(size)]

for i in range(size):
    mat_1[-1 - i].extend(mat[i])

for i in range(size):
    for j in range(size):
        print(mat_1[i][j], end=" ")
    print()

# Question 7
# Rotates a square matrix 90 degrees counterclockwise.
size = int(input())
mat = [[int(i) for i in input().split()] for _ in range(size)]
for i in range(size):
    for j in range(size):
        print(mat[-1 - j][i], end=" ")
    print()

# Question 8
# Simulates knight moves on a chessboard and prints possible moves.
desc = [["." for i in range(12)] for i in range(12)]
play = input()
if play[0] == "a":
    a, b = -int(play[1]) - 2, 2
if play[0] == "b":
    a, b = -int(play[1]) - 2, 3
if play[0] == "c":
    a, b = -int(play[1]) - 2, 4
if play[0] == "d":
    a, b = -int(play[1]) - 2, 5
if play[0] == "e":
    a, b = -int(play[1]) - 2, 6
if play[0] == "f":
    a, b = -int(play[1]) - 2, 7
if play[0] == "g":
    a, b = -int(play[1]) - 2, 8
if play[0] == "h":
    a, b = -int(play[1]) - 2, 9

desc[a][b] = "N"

desc[a - 2][b - 1] = "*" 
desc[a - 1][b - 2] = "*" 
desc[a + 2][b + 1] = "*" 
desc[a - 1][b + 2] = "*" 
desc[a - 2][b + 1] = "*" 
desc[a + 2][b - 1] = "*" 
desc[a + 1][b - 2] = "*" 
desc[a + 1][b + 2] = "*" 

for i in range(2, 10):
    for j in range(2, 10):
        print(desc[i][j], end=" ")
    print()

# Question 9
# Checks if a given matrix is a magic square.
n = int(input())
mat = [[int(i) for i in input().split()] for _ in range(n)]

flat_list = [item for sublist in mat for item in sublist]
flag = True
suum = sum(mat[0])

if len(flat_list) != len(set(flat_list)):
    flag = False
if flat_list.count(0) > 0:
    flag = False

for i in range(n):
    if sum(mat[i]) == suum:
        continue
    else:
        flag = False
        break

for i in range(n):
    suum_1 = 0
    for j in range(n):
        suum_1 += mat[j][i]
    if suum_1 != suum:
        flag = False
        break

suum_1 = 0
for i in range(n):
    suum_1 += mat[i][i]

if suum_1 != suum:
    flag = False

suum_1 = 0
for i in range(n):
    suum_1 += mat[-1 - i][-1 - i]

if suum_1 != suum:
    flag = False

if flag == True:
    print("YES")
else:
    print("NO")


# Part 3
# Question 1
# Creates a chessboard-like pattern of dots and asterisks.
codr = input().split()
mat = [["*" for _ in range(int(codr[1]))] for _ in range(int(codr[0]))]
for i in range(int(codr[0])):
    for j in range(int(codr[1])):
        if (i + j) % 2 == 0:
            mat[i][j] = "."

for i in range(int(codr[0])):
    print(*mat[i])

# Question 2
# Fills a square matrix with regions marked as 0, 1, or 2 based on their position.
size = int(input())
mat = [[0 for _ in range(size)] for _ in range(size)]
for i in range(size):
    for j in range(size):
        if (i < j and i < size - 1 - j) or (i > j and i < size - 1 - j) or (i == j and i < size - 1 - j):
            mat[i][j] = 0
        elif (i < j and i > size - 1 - j) or (i > j and i > size - 1 - j) or (i == j and i > size - 1 - j):
            mat[i][j] = 2
        else:
            mat[i][j] = 1

for i in range(size):
    print(*mat[i])

# Question 3
# Fills a matrix with numbers 1..n*m row by row, left to right.
size = input().split()
mat = [[0 for i in range(int(size[1]))] for _ in range(int(size[0]))]
a = 1
for i in range(int(size[0])):
    for j in range(int(size[1])):
        mat[i][j] = a
        a += 1
        print(str(mat[i][j]).ljust(3), end=" ")
    print()

# Question 4
# Fills a matrix column by column with consecutive numbers.
size = input().split()
mat = [[0 for i in range(int(size[1]))] for _ in range(int(size[0]))]

for i in range(int(size[0])):
    a = i + 1
    for j in range(int(size[1])):
        mat[i][j] = a
        a += int(size[0])
        print(str(mat[i][j]).ljust(3), end=" ")
    print()

# Question 5
# Fills diagonals of a square matrix with 1s, others remain 0.
size = int(input())
mat = [[0 for i in range(size)] for _ in range(size)]

for i in range(size):
    for j in range(size):
        if i == j:
            mat[i][j] = 1
        if i + j + 1 == size:
            mat[i][j] = 1
        print(str(mat[i][j]).ljust(3), end=" ")
    print()

# Question 6
# Fills diagonals and outer triangle regions with 1s in a square matrix.
size = int(input())
mat = [[0 for i in range(size)] for _ in range(size)]

for i in range(size):
    for j in range(size):
        if i == j:
            mat[i][j] = 1
        if j + i + 1 == size:
            mat[i][j] = 1
        if i < j and i < size - 1 - j or i > j and i > size - 1 - j:
            mat[i][j] = 1
        print(str(mat[i][j]).ljust(3), end=" ")
    print()

# Question 7
# Creates a matrix filled with numbers repeating in a sliding sequence across rows.
size = input().split()
mat = [[0 for i in range(int(size[1]))] for _ in range(int(size[0]))]
y = 0

for i in range(int(size[0])):
    if y > int(size[1]):
        y = 1
    if (i + 1) > int(size[1]):
        y += 1
        a = y
    else:
        a = i + 1
    for j in range(int(size[1])):
        if a > int(size[1]):
            a = 1
        mat[i][j] = a
        a += 1
        print(str(mat[i][j]).ljust(3), end=" ")
    print()

# Question 8
# Fills a matrix in a zigzag pattern (left-to-right, then right-to-left).
size, a = input().split(), 1
mat = [[0 for i in range(int(size[1]))] for _ in range(int(size[0]))]

for i in range(int(size[0])):
    if i % 2 == 0:
        for j in range(int(size[1])):
            mat[i][j] = a
            a += 1
    else:
        for j in range(int(size[1]) - 1, -1, -1):
            mat[i][j] = a
            a += 1
    for j in range(int(size[1])):
        print(str(mat[i][j]).ljust(3), end="")
    print()

# Question 9
# Fills a matrix diagonally with increasing numbers.
size, a = input().split(), 1
mat = [[0 for i in range(int(size[1]))] for _ in range(int(size[0]))]

for q in range(int(size[0]) * int(size[1])):
    for i in range(int(size[0])):
        for j in range(int(size[1])):
            if i + j == q:
                mat[i][j] = a
                a += 1
        
for i in range(int(size[0])):
    for j in range(int(size[1])):
        print(str(mat[i][j]).ljust(3), end="")
    print()

# Question 10
# Fills a matrix in spiral order with increasing numbers.
size = input().split()
mat = [[0 for i in range(int(size[1]))] for _ in range(int(size[0]))]

counter, lowm, highm, lown, highn = 1, 0, int(size[1]), 0, int(size[0])

if int(size[0]) > 1 and int(size[1]) > 1:
    while counter <= int(size[0]) * int(size[1]):
        for i in range(lowm, highm):
            mat[lown][i] = counter
            counter += 1
        lown += 1

        for i in range(lown, highn):
            mat[i][highm - 1] = counter
            counter += 1
        highm -= 1

        for i in range(highm - 1, lowm - 1, -1):
            mat[highn - 1][i] = counter
            counter += 1
        highn -= 1

        for i in range(highn - 1, lown - 1, -1):
            mat[i][lowm] = counter
            counter += 1
        lowm += 1

if int(size[0]) == 1 or int(size[1]) == 1:
    for i in range(int(size[0])):
        for j in range(int(size[1])):
            mat[i][j] = counter
            counter += 1

for i in range(int(size[0])):
    for j in range(int(size[1])):
        print(str(mat[i][j]).ljust(3), end=" ")
    print()