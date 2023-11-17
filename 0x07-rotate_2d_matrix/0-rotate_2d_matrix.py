#!/usr/bin/python3
'''
transforming matrix to 90 degree where position is been swapped
'''
def rotate_2d_matrix(matrix):
    size = len(matrix)
matrix = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]

size = len(matrix)
for i in range(size):
    for j in range(i, size):
        print(f"{i,j}")
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for array in matrix:
    array.reverse()

print(matrix)
