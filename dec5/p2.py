f = open("./input.txt", "r")
values = map(lambda x: int(x), f.readlines()[0].split(","))

def read(values, params, index, offset):
    if offset-1 < len(params):
        if params[offset-1] == "0":
            return values[values[index + offset]]
        elif params[offset-1] == "1":
            return values[index + offset]
    else:
        return values[values[index + offset]]

def evaluate(values, initial_input):
    index = 0
    while True:
        command = "0000000000" + str(values[index])
        opcode = int(command[-2:])
        params = command[:-2][::-1]

        if opcode == 99:
            break
        elif opcode == 1:
            value1 = read(values, params, index, 1)
            value2 = read(values, params, index, 2)
            values[values[index + 3]] = value1 + value2
            index += 4
        elif opcode == 2:
            value1 = read(values, params, index, 1)
            value2 = read(values, params, index, 2)
            values[values[index + 3]] = value1 * value2
            index += 4
        elif opcode == 3:
            values[values[index + 1]] = initial_input
            index += 2
        elif opcode == 4:
            print str(read(values, params, index, 1)) # useless output
            index += 2
        elif opcode == 5:
            value1 = read(values, params, index, 1)
            if (value1 != 0):
                index = read(values, params, index, 2)
            else:
                index += 3
        elif opcode == 6:
            value1 = read(values, params, index, 1)
            if (value1 == 0):
                index = read(values, params, index, 2)
            else:
                index += 3
        elif opcode == 7:
            value1 = read(values, params, index, 1)
            value2 = read(values, params, index, 2)
            if (value1 < value2):
                values[values[index + 3]] = 1
            else:
                values[values[index + 3]] = 0
            index += 4
        elif opcode == 8:
            value1 = read(values, params, index, 1)
            value2 = read(values, params, index, 2)
            if (value1 == value2):
                values[values[index + 3]] = 1
            else:
                values[values[index + 3]] = 0
            index += 4
        else:
            print opcode
            print "EEEK"
    return "Finished"

print evaluate(values, 5)
