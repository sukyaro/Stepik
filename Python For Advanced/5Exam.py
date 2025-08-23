
# Question 1
# Splits a list into N groups by distributing elements cyclically across sublists.
line, devide = input().split(), int(input())
line_1 = []
for i in range(devide):
    line_1.append([])
    for j in range(0 + i, len(line), devide):
        line_1[i].append(line[j])

print(line_1)

# Question 2
# Finds the maximum element inside the “hourglass-shaped” region of a square matrix.
size_of_the_mat = int(input())
mat = [input().split() for _ in range(size_of_the_mat)]
max = -1

for i in range(size_of_the_mat):
    for j in range(size_of_the_mat):
        if (i <= j and i > size_of_the_mat - 1 - j) or (i >= j and i > size_of_the_mat - 1 - j) or (i + j + 1 == size_of_the_mat):
            if int(mat[i][j]) > max:
                max = int(mat[i][j])
print(max)

# Question 3
# Prints the transpose of a square matrix.
size_of_the_mat = int(input())
mat = [input().split() for _ in range(size_of_the_mat)]

for i in range(size_of_the_mat):
    for j in range(size_of_the_mat):
        print(mat[j][i], end=" ")
    print()

# Question 4
# Draws a square matrix with “*” along both diagonals and the central row/column.
size_of_the_mat = int(input())
mat = [["." for _ in range(size_of_the_mat)] for _ in range(size_of_the_mat)]

for i in range(size_of_the_mat):
    for j in range(size_of_the_mat):
        if (i == j) or (i + j + 1 == size_of_the_mat) or (i == size_of_the_mat // 2) or (j == size_of_the_mat // 2):
            mat[i][j] = "*"

for i in range(size_of_the_mat):
    for j in range(size_of_the_mat):
        print(mat[i][j], end=" ")
    print()

# Question 5
# Checks if a square matrix is symmetric relative to its center (180° rotation).
size_of_the_mat = int(input())
mat = [input().split() for _ in range(size_of_the_mat)]
flag = True

for i in range(size_of_the_mat):
    for j in range(size_of_the_mat):
        if mat[i][j] != mat[size_of_the_mat - j - 1][size_of_the_mat - i - 1]:
            flag = False

if flag == True:
    print("YES")
else:
    print("NO")

# Question 6
# Checks if a square matrix is a Latin square (rows and columns contain 1..n exactly once).
size_of_the_mat = int(input())
mat = [[int(i) for i in input().split()] for _ in range(size_of_the_mat)]
flag = True

for i in range(size_of_the_mat):
    list_1, list_2 = [], []
    for j in range(size_of_the_mat):
        list_1.append(mat[i][j])
        list_2.append(mat[j][i])
    for m in range(1, size_of_the_mat + 1):
        if m not in list_1 or m not in list_2:
            flag = False

if flag == True:
    print("YES")
else:
    print("NO")

# Question 7
# Places a queen on a chessboard and marks all attacked squares.
mat = [["." for _ in range(8)] for _ in range(8)]
place = input()
slovarx = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
slovary = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}

for i in range(8):
    for j in range(8):
        if j == slovarx[place[0]] or i == slovary[place[1]]:
            mat[i][j] = "*"
        if i - j == slovary[place[1]] - slovarx[place[0]] or i + j == slovarx[place[0]] + slovary[place[1]]:
            mat[i][j] = "*"

mat[slovary[place[1]]][slovarx[place[0]]] = "Q"
for i in range(8):
    for j in range(8):
        print(mat[i][j], end=" ")
    print()

# Question 8
# Fills a square matrix so that diagonals are numbered by their distance from the main diagonal.
size = int(input())
mat = [[0 for _ in range(size)] for _ in range(size)]

for i in range(size):
    for j in range(size):
        for m in range(size):
            if i == j - m or i == m - j:
                mat[j][m] = i

for i in range(size):
    for j in range(size):
        print(mat[i][j], end=" ")
    print()