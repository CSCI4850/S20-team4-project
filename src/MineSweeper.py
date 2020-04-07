#!/usr/bin/python3

import random
import csv
import re
import time
from string import ascii_lowercase


def setupgrid(gridsize, start, numberofmines):
    # Initialize empty grid
    emptygrid = [['0' for i in range(gridsize)] for i in range(gridsize)]
    
    mines = getmines(emptygrid, start, numberofmines)
    
    # Label mine spaces
    for i, j in mines:
        emptygrid[i][j] = 'X'

    grid = getnumbers(emptygrid)

    return (grid, mines)

# Output the grid
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
            row = str(row) + ' ' + str(j) + ' |'

        print(row + '\n' + horizontal)

    print('')


def getrandomcell(grid):
    gridsize = len(grid)

    a = random.randint(0, gridsize - 1)
    b = random.randint(0, gridsize - 1)

    return (a, b)

# Used to initialize neighboring cells / safe cells
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

# Once the neighbors are initialized, this fills in random remaining spaces,
# excluding the starting cell and neighbors, up to the requested number of mines
def getmines(grid, start, numberofmines):
    mines = []
    neighbors = getneighbors(grid, *start) # initialize unavailable spaces

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

    # Reformat input for more flexible acceptance
    pattern = r'([a-{}])([0-9]+)(f?)'.format(ascii_lowercase[gridsize - 1])
    validinput = re.match(pattern, inputstring)

    # Enter input into the associated grid space
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
    newgrid = csvload(grid)
    with open ('grid.csv', mode='w') as grid_file:
        file_writer = csv.writer(grid_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow([newgrid[0][0], newgrid[0][1], newgrid[0][2], newgrid[0][3], newgrid[0][4], newgrid[0][5], newgrid[0][6], newgrid[0][7], newgrid[0][8]])
        file_writer.writerow([newgrid[1][0], newgrid[1][1], newgrid[1][2], newgrid[1][3], newgrid[1][4], newgrid[1][5], newgrid[1][6], newgrid[1][7], newgrid[1][8]])
        file_writer.writerow([newgrid[2][0], newgrid[2][1], newgrid[2][2], newgrid[2][3], newgrid[2][4], newgrid[2][5], newgrid[2][6], newgrid[2][7], newgrid[2][8]])
        file_writer.writerow([newgrid[3][0], newgrid[3][1], newgrid[3][2], newgrid[3][3], newgrid[3][4], newgrid[3][5], newgrid[3][6], newgrid[3][7], newgrid[3][8]])
        file_writer.writerow([newgrid[4][0], newgrid[4][1], newgrid[4][2], newgrid[4][3], newgrid[4][4], newgrid[4][5], newgrid[4][6], newgrid[4][7], newgrid[4][8]])
        file_writer.writerow([newgrid[5][0], newgrid[5][1], newgrid[5][2], newgrid[5][3], newgrid[5][4], newgrid[5][5], newgrid[5][6], newgrid[5][7], newgrid[5][8]])
        file_writer.writerow([newgrid[6][0], newgrid[6][1], newgrid[6][2], newgrid[6][3], newgrid[6][4], newgrid[6][5], newgrid[6][6], newgrid[6][7], newgrid[6][8]])
        file_writer.writerow([newgrid[7][0], newgrid[7][1], newgrid[7][2], newgrid[7][3], newgrid[7][4], newgrid[7][5], newgrid[7][6], newgrid[7][7], newgrid[7][8]])
        file_writer.writerow([newgrid[8][0], newgrid[8][1], newgrid[8][2], newgrid[8][3], newgrid[8][4], newgrid[8][5], newgrid[8][6], newgrid[8][7], newgrid[8][8]])
    grid_file.close()

def csvload(grid):
    newgrid = grid
    for x in range(0,9):
        for y in range(0,9):
            if grid[x][y] == 0:
                newgrid[x][y] = 0.0
            if grid[x][y] == 1:
                newgrid[x][y] = 0.125
            if grid[x][y] == 2:
                newgrid[x][y] = 0.25
            if grid[x][y] == 3:
                newgrid[x][y] = 0.375
            if grid[x][y] == 4:
                newgrid[x][y] = 0.5
            if grid[x][y] == 5:
                newgrid[x][y] = 0.625
            if grid[x][y] == 6:
                newgrid[x][y] = 0.75
            if grid[x][y] == 7:
                newgrid[x][y] = 0.875
            if grid[x][y] == 8:
                newgrid[x][y] = 1
            if grid[x][y] == ' ':
                newgrid[x][y] = -1
    return newgrid
     
def promptread():
    fstream=open('response.txt','r')
    thing = fstream.read()
    fstream.close()
    return thing

#
def feedbackload(flagcheck):
    fstream=open('response.txt','w')
    fstream.write(flagcheck)
    fstream.close()

def playgame():
    gridsize = 9
    numberofmines = 10
    flagcheck = True

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
        
        #implementation of neural net portion
        tempgrid = [row[:]for row in currgrid]
        csvpush(tempgrid)

        prompt = input('Enter the cell ({} mines left): '.format(minesleft))
        #prompt=promptread()
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
                flagcheck=False
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

        print(message)

playgame()

