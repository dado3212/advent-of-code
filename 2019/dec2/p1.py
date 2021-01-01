f = open("./input.txt", "r")
values = map(lambda x: int(x), f.readlines()[0].split(","))
values[1] = 12
values[2] = 2

index = 0
while True:
    opcode = values[index]
    if opcode == 99:
        break
    value1 = values[values[index+1]]
    value2 = values[values[index+2]]
    new_pos = values[index+3]
    if opcode == 1:
        values[new_pos] = value1 + value2
    elif opcode == 2:
        values[new_pos] = value1 * value2
    index += 4
print values[0]
