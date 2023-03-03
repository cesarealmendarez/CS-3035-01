'''
    Cesar Almendarez
    CSULA Spring 2023
    CS 3035-01 Programming Paradigms
    Lab 12 (Multidimensional Arrays) 
    March 2 2023
'''

# Iterate through each matrix element using nested for loops. For each element in matrix A; add it to the corresponding element in the matrix B 
def matrixAdd(A, B, SUM):
    for i in range(len(A)):
        for j in range(len(A[0])):
            SUM[i][j] = A[i][j] + B[i][j]

    return SUM

# Iterate through each matrix element using nested for loops. For each element in Matrix A; concatonate with the corresponding element in Matrix B
def matrixAddAsString(A, B, SUM):
    for i in range(len(A)):
        for j in range(len(A[0])):
            SUM[i][j] = str(A[i][j]) + str(B[i][j])
    
    return SUM

# Initialize matrices A, B, SUM
A = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

B = [[3, 3, 3], [2, 2, 2], [1, 1, 1]]

SUM = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Print return values of matrixAdd() and matrixAddAsString
print(matrixAdd(A, B, SUM))

print(matrixAddAsString(A, B, SUM))

