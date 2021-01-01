import math, re

class Grid:
    def __init__(self, raw_map):
        self.grid = self.__buildGrid(raw_map)
        self.r = 0
        self.c = 0
        self.w = len(self.grid[0])
        self.h = len(self.grid)
        self.outOfBounds = False

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
        self.outOfBounds = (row > self.h or col > self.w)
        self.r = row
        self.c = col

    def movePos(self, row, col):
        self.r = self.r + row
        self.c = (self.c + col) % self.w
        self.outOfBounds = (self.r >= self.h or col >= self.w)

    def isTree(self):
        return self.grid[self.r][self.c] == "#"

    def isOutOfBounds(self):
        return self.outOfBounds

valid = 0
with open("./input.txt", "r") as f:
    moves = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    all = 1
    grid = Grid(f.readlines())
    for move in moves:
        grid.setPos(0, 0)
        trees = 0
        while not grid.isOutOfBounds():
            trees += grid.isTree()
            grid.movePos(move[0], move[1])

        all *= trees
    print all
