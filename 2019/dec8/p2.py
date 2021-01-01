f = open("./input.txt", "r")
value = f.readlines()[0]
#value = "0222112222120000"
width = 25 #2
height = 6  #2

def layerify(raw, w, h):
    layers = []
    layer = []
    row = []
    for i in range(0, len(raw)):
        row.append(raw[i])
        if (i + 1) % w == 0:
            layer.append(row)
            row = []
        if (i + 1) % (w * h) == 0:
            layers.append(layer)
            layer = []
    return layers


def render(layers, w, h):
    row = ""
    for y in range(0, h):
        for x in range(0, w):
            for layer in layers:
                if layer[y][x] == "1":
                    row += "*"
                    break
                elif layer[y][x] == "0":
                    row += " "
                    break
        print row
        row = ""
    print row

layers = layerify(value, width, height)
render(layers, width, height)
