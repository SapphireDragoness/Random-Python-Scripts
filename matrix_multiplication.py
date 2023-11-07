from math import ceil, log
import numpy as np
import time

def randomMatrix(size):
    return np.random.randint(1, 100, (size, size))

def standardMultiplication(matrix1, matrix2):
    n = len(matrix1)
    product = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                product[i][j] += matrix1[i][k] * matrix2[k][j]
    return product

def numpyMultiplication(matrix1, matrix2):
    return matrix1*matrix2

def add(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] + B[i][j]
    return C


def subtract(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] - B[i][j]
    return C


def strassenR(A, B):
    n = len(A)

    if n <= 10:
        return standardMultiplication(A, B)
    else:
        # initializing the new sub-matrices
        new_size = n // 2
        a11 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        a12 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        a21 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        a22 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]

        b11 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        b12 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        b21 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        b22 = [[0 for j in range(0, new_size)] for i in range(0, new_size)]

        aResult = [[0 for j in range(0, new_size)] for i in range(0, new_size)]
        bResult = [[0 for j in range(0, new_size)] for i in range(0, new_size)]

        # dividing the matrices in 4 sub-matrices:
        for i in range(0, new_size):
            for j in range(0, new_size):
                a11[i][j] = A[i][j]  # top left
                a12[i][j] = A[i][j + new_size]  # top right
                a21[i][j] = A[i + new_size][j]  # bottom left
                a22[i][j] = A[i + new_size][j + new_size]  # bottom right

                b11[i][j] = B[i][j]  # top left
                b12[i][j] = B[i][j + new_size]  # top right
                b21[i][j] = B[i + new_size][j]  # bottom left
                b22[i][j] = B[i + new_size][j + new_size]  # bottom right

        # Calculating p1 to p7:
        aResult = add(a11, a22)
        bResult = add(b11, b22)
        p1 = strassenR(aResult, bResult)  # p1 = (a11+a22) * (b11+b22)

        aResult = add(a21, a22)  # a21 + a22
        p2 = strassenR(aResult, b11)  # p2 = (a21+a22) * (b11)

        bResult = subtract(b12, b22)  # b12 - b22
        p3 = strassenR(a11, bResult)  # p3 = (a11) * (b12 - b22)

        bResult = subtract(b21, b11)  # b21 - b11
        p4 = strassenR(a22, bResult)  # p4 = (a22) * (b21 - b11)

        aResult = add(a11, a12)  # a11 + a12
        p5 = strassenR(aResult, b22)  # p5 = (a11+a12) * (b22)

        aResult = subtract(a21, a11)  # a21 - a11
        bResult = add(b11, b12)  # b11 + b12
        p6 = strassenR(aResult, bResult)  # p6 = (a21-a11) * (b11+b12)

        aResult = subtract(a12, a22)  # a12 - a22
        bResult = add(b21, b22)  # b21 + b22
        p7 = strassenR(aResult, bResult)  # p7 = (a12-a22) * (b21+b22)

        # calculating c21, c21, c11 e c22:
        c12 = add(p3, p5)  # c12 = p3 + p5
        c21 = add(p2, p4)  # c21 = p2 + p4

        aResult = add(p1, p4)  # p1 + p4
        bResult = add(aResult, p7)  # p1 + p4 + p7
        c11 = subtract(bResult, p5)  # c11 = p1 + p4 - p5 + p7

        aResult = add(p1, p3)  # p1 + p3
        bResult = add(aResult, p6)  # p1 + p3 + p6
        c22 = subtract(bResult, p2)  # c22 = p1 + p3 - p2 + p6

        # Grouping the results obtained in a single matrix:
        C = [[0 for j in range(0, n)] for i in range(0, n)]
        for i in range(0, new_size):
            for j in range(0, new_size):
                C[i][j] = c11[i][j]
                C[i][j + new_size] = c12[i][j]
                C[i + new_size][j] = c21[i][j]
                C[i + new_size][j + new_size] = c22[i][j]
        return C


def strassen(A, B):
    # Make the matrices bigger so that you can apply the strassen
    # algorithm recursively without having to deal with odd
    # matrix sizes
    nextPowerOfTwo = lambda n: 2 ** int(ceil(log(n, 2)))
    n = len(A)
    m = nextPowerOfTwo(n)
    APrep = [[0 for i in range(m)] for j in range(m)]
    BPrep = [[0 for i in range(m)] for j in range(m)]
    for i in range(n):
        for j in range(n):
            APrep[i][j] = A[i][j]
            BPrep[i][j] = B[i][j]
    CPrep = strassenR(APrep, BPrep)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = CPrep[i][j]
    return C
    

size = input("Enter matrix size: ")

matrix1 = randomMatrix(int(size))
matrix2 = randomMatrix(int(size))

print(f"Matrix 1: \n{matrix1}")
print(f"Matrix 2: \n{matrix2}")

t1 = time.perf_counter()
product = standardMultiplication(matrix1, matrix2)
t2 = time.perf_counter()

print(f"Standard multiplication: {t2-t1}")
#print(f"Product: \n{product}")

t1 = time.perf_counter()
strassen(matrix1, matrix2)
t2 = time.perf_counter()

print(f"Strassen multiplication: {t2-t1}")
#print(f"Product: \n{product}")

t1 = time.perf_counter()
numpyMultiplication(matrix1, matrix2)
t2 = time.perf_counter()

print(f"Numpy multiplication: {t2-t1}")
#print(f"Product: \n{product}")

