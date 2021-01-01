import math, re

def is_valid(password):
    a = re.search(r"(\d+)-(\d+) (.): (.*)", password)
    char = a.group(3)
    password = a.group(4)
    num_times = password.count(char)
    return num_times >= int(a.group(1)) and num_times <= int(a.group(2))

valid = 0
with open("./input.txt", "r") as f:
    for x in f.readlines():
        valid += is_valid(x)

print valid
