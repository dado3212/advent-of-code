from itertools import permutations

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

def run(values, amp_input, setting = None):
    index = 0
    while True:
        command = "0000000000" + str(values[index])
        opcode = int(command[-2:])
        params = command[:-2][::-1]

        if opcode == 99:
            print "breaking"
            return -1
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
            if setting != None:
                new_val = setting
                setting = None
            elif amp_input != -1:
                new_val = amp_input
                amp_input = -1
            else:
                print "Trying to read a third time, erroring."
                break
            values[values[index + 1]] = new_val
            index += 2
        elif opcode == 4:
            output = read(values, params, index, 1) # useless output
            amp_input = output
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
    return amp_input

def maximize_output(values):
    best_output = 0
    for permutation in permutations([5, 6, 7, 8, 9]):
        # first run
        a = run(values, 0, permutation[0])
        b = run(values, a, permutation[1])
        c = run(values, b, permutation[2])
        d = run(values, c, permutation[3])
        e = run(values, d, permutation[4])
        if e > best_output:
            best_output = e
        # looped run
        while (True):
            a = run(values, e)
            b = run(values, a)
            c = run(values, b)
            d = run(values, c)
            e = run(values, d)
            if e > best_output:
                best_output = e
            elif e == -1:
                break
    return best_output

print maximize_output(values)
