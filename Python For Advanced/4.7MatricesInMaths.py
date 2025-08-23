
import copy


# Question 1
# Reads two matrices of the same size, adds them element-wise, and prints the resulting matrix.
size = input().split()
a = [input().split() for _ in range(int(size[0]))]
input()
b = [input().split() for _ in range(int(size[0]))]
c = []

for i in range(int(size[0])):
    c.append([])
    for j in range(int(size[1])):
        c[i].append(int(a[i][j]) + int(b[i][j]))
    
for i in range(int(size[0])):
    for j in range(int(size[1])):
        print(c[i][j], end=" ")
    print()

# Question 2
# Reads two matrices and computes their product (matrix multiplication).
size_for_mat_a = input().split()
a = [input().split() for _ in range(int(size_for_mat_a[0]))]
input()

size_for_mat_b = input().split()
b = [input().split() for _ in range(int(size_for_mat_b[0]))]
c = []

for m in range(int(size_for_mat_a[0])):
    c.append([])
    for i in range(int(size_for_mat_a[0])):
        adding_bit = 0
        for j in range(int(size_for_mat_b[0])):
            adding_bit += int(a[m][j]) * int(b[j][i])
        c[m].append(adding_bit)

for i in range(int(size_for_mat_a[0])):
    for j in range(int(size_for_mat_b[1])):
        print(c[i][j], end=" ")
    print()

# Question 3
# Raises a square matrix to a given power (by repeated multiplication) and prints the result.
size_for_mat = int(input())
a = [input().split() for _ in range(size_for_mat)]
multiply = int(input()) - 1
c = copy.deepcopy(a)

for counter in range(multiply):
    d = []
    for m in range(size_for_mat):
        d.append([])
        for i in range(size_for_mat):
            adding_bit = 0
            for j in range(size_for_mat):
                adding_bit += int(a[m][j]) * int(c[j][i])
            d[m].append(adding_bit)
    c = copy.deepcopy(d)

for i in range(size_for_mat):
    for j in range(size_for_mat):
        print(d[i][j], end=" ")
    print()
