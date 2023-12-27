import numpy as np

def enterSudoku():
    sudoku = np.zeros((9,9))

    for i in range(9):
        for j in range(9):
            n = input(f"Enter sudoku cell [{i}, {j}]: ")
            sudoku.itemset((i,j), n)
    return sudoku

def printSudoku(sudoku):
    for i in range(0,9):
        for j in range(0,9):
            print(sudoku[i][j])

def findEmpty(sudoku):
    for i in range(0,9):
        for j in range(0,9):
            if sudoku[i][j] == 0:
                return (i, j)
    return None

def isValid(sudoku, n, r, c):
    for i in range(0,9):
        if sudoku[r][i] == n and c != i:
            return False
    for i in range(0,9):
        if sudoku[i][c] == n and r != i:
            return False

    x = c // 3
    y = r // 3

    for i in range(y*3, y*3+3):
        for j in range(x*3, x*3+3):
            if sudoku[i][j] == n and i != r and j != c:
                return False 

def solveSudoku(sudoku):
    if not findEmpty(sudoku):
        return True
    else: 
        r, c = findEmpty(sudoku)
    
    for i in range(1,10):
        if isValid(sudoku, i, r, c):
            sudoku[r][c] = i
            if solveSudoku(sudoku):
                return True
            sudoku[r][c] = 0
    return False

sudoku = enterSudoku()
print(f"Your sudoku: {printSudoku(sudoku)}")
solveSudoku(sudoku)
print(f"Solved sudoku: {printSudoku(sudoku)}")
        
