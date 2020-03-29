#!/usr/bin/python3

import random
import csv
import re
import time
from string import ascii_lowercase


def setupgrid(gridsize, start, numberofmines):
    emptygrid = [['0' for i in range(gridsize)] for i in range(gridsize)]

    mines = getmines(emptygrid, start, numberofmines)

    for i, j in mines:
        emptygrid[i][j] = 'X'

    grid = getnumbers(emptygrid)

    return (grid, mines)


def showgrid(grid):
    gridsize = len(grid)

    horizontal = '   ' + (4 * gridsize * '-') + '-'

    # Print top column letters
    toplabel = '     '

    for i in ascii_lowercase[:gridsize]:
        toplabel = toplabel + i + '   '

    print(toplabel + '\n' + horizontal)

    # Print left row numbers
    for idx, i in enumerate(grid):
        row = '{0:2} |'.format(idx + 1)

        for j in i:
            row = row + ' ' + j + ' |'

        print(row + '\n' + horizontal)

    print('')


def getrandomcell(grid):
    gridsize = len(grid)

    a = random.randint(0, gridsize - 1)
    b = random.randint(0, gridsize - 1)

    return (a, b)


def getneighbors(grid, rowno, colno):
    gridsize = len(grid)
    neighbors = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            elif -1 < (rowno + i) < gridsize and -1 < (colno + j) < gridsize:
                neighbors.append((rowno + i, colno + j))

    return neighbors


def getmines(grid, start, numberofmines):
    mines = []
    neighbors = getneighbors(grid, *start)

    for i in range(numberofmines):
        cell = getrandomcell(grid)
        while cell == start or cell in mines or cell in neighbors:
            cell = getrandomcell(grid)
        mines.append(cell)

    return mines


def getnumbers(grid):
    for rowno, row in enumerate(grid):
        for colno, cell in enumerate(row):
            if cell != 'X':
                # Gets the values of the neighbors
                values = [grid[r][c] for r, c in getneighbors(grid,
                                                              rowno, colno)]

                # Counts how many are mines
                grid[rowno][colno] = str(values.count('X'))

    return grid


def showcells(grid, currgrid, rowno, colno):
    # Exit function if the cell was already shown
    if currgrid[rowno][colno] != ' ':
        return

    # Show current cell
    currgrid[rowno][colno] = grid[rowno][colno]

    # Get the neighbors if the cell is empty
    if grid[rowno][colno] == '0':
        for r, c in getneighbors(grid, rowno, colno):
            # Repeat function for each neighbor that doesn't have a flag
            if currgrid[r][c] != 'F':
                showcells(grid, currgrid, r, c)


def playagain():
    choice = input('Play again? (y/n): ')

    return choice.lower() == 'y'


def parseinput(inputstring, gridsize, helpmessage):
    cell = ()
    flag = False
    message = "Invalid cell. " + helpmessage

    pattern = r'([a-{}])([0-9]+)(f?)'.format(ascii_lowercase[gridsize - 1])
    validinput = re.match(pattern, inputstring)

    if inputstring == 'help':
        message = helpmessage

    elif validinput:
        rowno = int(validinput.group(2)) - 1
        colno = ascii_lowercase.index(validinput.group(1))
        flag = bool(validinput.group(3))

        if -1 < rowno < gridsize:
            cell = (rowno, colno)
            message = ''

    return {'cell': cell, 'flag': flag, 'message': message}


def csvpush(grid):
    grid = csvload(grid)
    with open ('grid.csv', mode='w') as grid_file:
        file_writer = csv.writer(grid_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow([grid[0][0], grid[0][1], grid[0][2], grid[0][3], grid[0][4], grid[0][5], grid[0][6], grid[0][7], grid[0][8]])
        file_writer.writerow([grid[1][0], grid[1][1], grid[1][2], grid[1][3], grid[1][4], grid[1][5], grid[1][6], grid[1][7], grid[1][8]])
        file_writer.writerow([grid[2][0], grid[2][1], grid[2][2], grid[2][3], grid[2][4], grid[2][5], grid[2][6], grid[2][7], grid[2][8]])
        file_writer.writerow([grid[3][0], grid[3][1], grid[3][2], grid[3][3], grid[3][4], grid[3][5], grid[3][6], grid[3][7], grid[3][8]])
        file_writer.writerow([grid[4][0], grid[4][1], grid[4][2], grid[4][3], grid[4][4], grid[4][5], grid[4][6], grid[4][7], grid[4][8]])
        file_writer.writerow([grid[5][0], grid[5][1], grid[5][2], grid[5][3], grid[5][4], grid[5][5], grid[5][6], grid[5][7], grid[5][8]])
        file_writer.writerow([grid[6][0], grid[6][1], grid[6][2], grid[6][3], grid[6][4], grid[6][5], grid[6][6], grid[6][7], grid[6][8]])
        file_writer.writerow([grid[7][0], grid[7][1], grid[7][2], grid[7][3], grid[7][4], grid[7][5], grid[7][6], grid[7][7], grid[7][8]])
        file_writer.writerow([grid[8][0], grid[8][1], grid[8][2], grid[8][3], grid[8][4], grid[8][5], grid[8][6], grid[8][7], grid[8][8]])

def csvload(grid):
    for x in range(0,9):
        for y in range(0,9):
            if grid[x][y] == 0:
                grid[x][y] = 0.0
            if grid[x][y] == 1:
                grid[x][y] = 0.125
            if grid[x][y] == 2:
                grid[x][y] = 0.25
            if grid[x][y] == 3:
                grid[x][y] = 0.375
            if grid[x][y] == 4:
                grid[x][y] = 0.5
            if grid[x][y] == 5:
                grid[x][y] = 0.625
            if grid[x][y] == 6:
                grid[x][y] = 0.75
            if grid[x][y] == 7:
                grid[x][y] = 0.875
            if grid[x][y] == 8:
                grid[x][y] = 1
            if grid[x][y] == ' ':
                grid[x][y] = -1
    
    return grid
     


def playgame():
    gridsize = 9
    numberofmines = 10

    currgrid = [[' ' for i in range(gridsize)] for i in range(gridsize)]

    grid = []
    flags = []
    starttime = 0

    helpmessage = ("Type the column followed by the row (eg. a5). "
                   "To put or remove a flag, add 'f' to the cell (eg. a5f).")

    showgrid(currgrid)
    print(helpmessage + " Type 'help' to show this message again.\n")

    while True:
        minesleft = numberofmines - len(flags)
        prompt = input('Enter the cell ({} mines left): '.format(minesleft))
        result = parseinput(prompt, gridsize, helpmessage + '\n')

        message = result['message']
        cell = result['cell']

        if cell:
            print('\n\n')
            rowno, colno = cell
            currcell = currgrid[rowno][colno]
            flag = result['flag']

            if not grid:
                grid, mines = setupgrid(gridsize, cell, numberofmines)
            if not starttime:
                starttime = time.time()

            if flag:
                # Add a flag if the cell is empty
                if currcell == ' ':
                    currgrid[rowno][colno] = 'F'
                    flags.append(cell)
                # Remove the flag if there is one
                elif currcell == 'F':
                    currgrid[rowno][colno] = ' '
                    flags.remove(cell)
                else:
                    message = 'Cannot put a flag there'

            # If there is a flag there, show a message
            elif cell in flags:
                message = 'There is a flag there'

            elif grid[rowno][colno] == 'X':
                print('Game Over\n')
                showgrid(grid)
                if playagain():
                    playgame()
                return

            elif currcell == ' ':
                showcells(grid, currgrid, rowno, colno)

            else:
                message = "That cell is already shown"

            if set(flags) == set(mines):
                minutes, seconds = divmod(int(time.time() - starttime), 60)
                print(
                    'You Win. '
                    'It took you {} minutes and {} seconds.\n'.format(minutes,
                                                                      seconds))
                showgrid(grid)
                if playagain():
                    playgame()
                return

        showgrid(currgrid)
        csvpush(currgrid)
        print(message)

playgame()

