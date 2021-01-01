def number_is_valid(num):
    num = str(num)
    split_by_num = []
    current = ""
    for i in range(0, len(num)):
        if current == "" or num[i] == current[0]:
            current = current + num[i]
        else:
            split_by_num.append(current)
            current = num[i]
    split_by_num.append(current)
    return any(len(x) == 2 for x in split_by_num) and sorted(split_by_num) == split_by_num

num_range = range(168630, 718098+1)
count = 0
for i in num_range:
    if number_is_valid(i):
        count += 1
print count
