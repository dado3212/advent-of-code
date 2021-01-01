import math

all_nums = {}
with open("./input.txt", "r") as f:
    for x in f.readlines():
        num = int(x)
        if (2020 - num) in all_nums:
            print num * (2020 - num)
        all_nums[num] = 1
