def ptToString(point):
    return str(point[0]) + "," + str(point[1])

def strToPoint(str):
    v = str.split(",")
    return [int(v[0]), int(v[1])]

def directions_to_positions(input):
    position = [0, 0]
    all_positions = []
    for direction in input.split(","):
        way = direction[0]
        distance = int(direction[1:])
        if way == "U":
            modifier = [0, 1]
        elif way == "D":
            modifier = [0, -1]
        elif way == "L":
            modifier = [-1, 0]
        elif way == "R":
            modifier = [1, 0]
        else:
            print "WHAT IS THIS"
            break
        for i in range(0, distance):
            position = [position[0] + modifier[0], position[1] + modifier[1]]
            all_positions.append(position)

    return set([ptToString(x) for x in all_positions])

f = open("./input.txt", "r")
values = f.readlines()
d1 = directions_to_positions(values[0])
d2 = directions_to_positions(values[1])
intersection = [strToPoint(x) for x in d1.intersection(d2)]
print min([abs(x[0]) + abs(x[1]) for x in intersection])
