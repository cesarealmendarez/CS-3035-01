'''
    Assignment: Lab 12(Multidimensional Arrays) 
    File: lab12.py
    Authored By: Cesar E Almendarez
    Written On: March 2 2023
'''

def matrixAdd(A, B, SUM):

    for i in range(len(A)):
        for j in range(len(A[0])):
            SUM[i][j] = A[i][j] + B[i][j]

    return SUM

def matrixAddAsString(A, B, SUM):
    for i in range(len(A)):
        for j in range(len(A[0])):
            SUM[i][j] = str(A[i][j]) + str(B[i][j])

    return SUM

A = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

B = [[3, 3, 3], [2, 2, 2], [1, 1, 1]]

SUM = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

SUM2 = [['', '', ''], ['', '', '']]

print(matrixAdd(A, B, SUM))

print(matrixAddAsString(A, B, SUM))

