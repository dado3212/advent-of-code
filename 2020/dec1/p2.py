import math

all_nums = {}
with open("./input.txt", "r") as f:
    for x in f.readlines():
        num = int(x)
        all_nums[num] = 1

for num1 in all_nums:
    for num2 in all_nums:
        if (2020 - num1 - num2) in all_nums:
            print num1 * num2 * (2020 - num1 - num2)
            exit()
