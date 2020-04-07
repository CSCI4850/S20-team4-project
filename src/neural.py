import random
import csv
import re
import time
from string import ascii_lowercase

def readcsv(grid):
    with open('grid.csv') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        x = 0
        
        for row in csv_reader:
            grid.append(row)
            x+=1
        return grid

def writeresponse(val):
    txtfile=open("response.txt","w")
    txtfile.write(val)
    txtfile.close()

def main():
    grid=[]
    grid = readcsv(grid)
    print(grid)
    # some neural nets stuff
    val = 'a1'
    writeresponse(val)

main()