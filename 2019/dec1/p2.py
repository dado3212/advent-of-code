import math

def fuel(mass):
    total = 0
    while True:
        new = int(math.floor(mass / 3)) - 2
        if new <= 0:
            break
        else:
            total += new
            mass = new
    return total

total = 0
with open("./input.txt", "r") as f:
    for x in f.readlines():
        total += fuel(int(x[:-1]))

print total
