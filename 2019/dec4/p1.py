def number_is_valid(num):
    num = str(num)
    found_pair = False
    for i in range(0, len(num) - 1):
        if num[i] == num[i+1]:
            found_pair = True
        if int(num[i]) > int(num[i+1]):
            return False
    return found_pair

num_range = range(168630, 718098+1)
count = 0
for i in num_range:
    if number_is_valid(i):
        count += 1
print count
