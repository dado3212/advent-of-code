f = open("./input.txt", "r")
values = map(lambda x: int(x), f.readlines()[0].split(","))

def evaluate(values, noun, verb):
    values[1] = noun
    values[2] = verb

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
    return values[0]

for noun in range(0, 100):
    for verb in range(0, 100):
        if evaluate(values[:], noun, verb) == 19690720:
            print str(noun) + ", " + str(verb) + ", " + str(100 * noun + verb)
