import math

def fuel(mass):
    return int(math.floor(mass / 3)) - 2

total = 0
with open("./input.txt", "r") as f:
    for x in f.readlines():
        total += fuel(int(x[:-1]))

print total
