import math, re

class Grid:
    def __init__(self, raw_map):
        self.grid = self.__buildGrid(raw_map)
        self.r = 0
        self.c = 0
        self.w = len(self.grid[0])
        self.h = len(self.grid)

    def __buildGrid(self, raw_map):
        grid = []
        for row in raw_map:
            new_row = []
            for char in row:
                if char != "\n":
                    new_row.append(char)
            grid.append(new_row)
        return grid

    def __str__(self):
        output = ""
        for row in self.grid:
            output += "".join(row) + "\n"
        return output

    def getPos(self):
        return (self.r, self.c)

    def setPos(self, row, col):
        self.r = row
        self.c = col

    def movePos(self, row, col):
        self.r = (self.r + row) % self.h
        self.c = (self.c + col) % self.w

    def isTree(self):
        return self.grid[self.r][self.c] == "#"

valid = 0
with open("./input.txt", "r") as f:
    grid = Grid(f.readlines())
    grid.setPos(0, 0)
    trees = 0
    start = True
    while grid.getPos()[0] != 0 or start:
        start = False
        grid.movePos(1, 3)
        trees += grid.isTree()
    print trees
