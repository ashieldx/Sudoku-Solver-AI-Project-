import pyautogui
import math
import time
import numpy

grid = []

def autoprint():
    global grid

    temp = []
        
    for i in range(9):
        temp.append(grid[i])

    solution = []

    for i in temp:
        for j in i:
            solution.append(str(j))

    counter = 0
    
    for i in solution:
        pyautogui.hotkey(i)
        pyautogui.hotkey('right')
        counter = counter + 1

        if counter == 9:
            counter = 0
            pyautogui.hotkey('down')
            for i in range(9):
                pyautogui.hotkey('left')

def consoleprint():
    global grid
    print(numpy.matrix(grid))

def check(x, y, n):

    for i in range(9):
        if grid[i][y] == n:
            return False

    for i in range(9):
        if grid[x][i] == n:
            return False

    for i in range(math.floor(x/3)*3, math.floor(x/3)*3 + 3):
        for j in range(math.floor(y/3)*3, math.floor(y/3)*3 + 3):  
            if grid[i][j] == n:
                return False
    return True

def solver():
    global grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for k in range(9):
                    if check(i, j, k+1):
                        grid[i][j] = k+1
                        solver()
                        grid[i][j] = 0
                return
    
    print("Your Sudoku Solution:")
    consoleprint()

    inp = input("Auto input to sudoku.com [Y/N]? ")

    if inp == 'Y':
        print("Click the top left box on sudoku.com")
        time.sleep(2)
        autoprint()

def main():
    global grid

    print("Input your Sudoku by row")

    for i in range(9):
        row = []
        print("Row ", i+1, ": ")
        sudoku_row = list(input())
        
        for n in sudoku_row:
            row.append(int(n))
        grid.append(row)

    solver()

main()