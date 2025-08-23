
# Question 1
# Create a matrix of given size filled with a specified element (default 0)
def matrix(size1=1, size2=None, element=0):
    if size2 == None:
        size2 = size1  # Make it square if only one size is given

    matrix = [[element for _ in range(size2)] for _ in range(size1)]
    return matrix

print(matrix())         # 1x1 matrix filled with 0
print(matrix(3))        # 3x3 matrix filled with 0
print(matrix(2, 5))     # 2x5 matrix filled with 0
print(matrix(3, 4, 9))  # 3x4 matrix filled with 9
