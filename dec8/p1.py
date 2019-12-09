f = open("./input.txt", "r")
value = f.readlines()[0]

def layerify(raw, w, h):
    layers = []
    layer = []
    for i in range(0, len(raw)):
        layer.append(raw[i])
        if (i+1) % (w * h) == 0:
            layers.append(layer)
            layer = []
    return layers

layers = layerify(value, 25, 6)
fewest_zero = -1
best = []
for layer in layers:
    num_zeroes = sum(1 for x in layer if x == "0")
    if num_zeroes < fewest_zero or fewest_zero == -1:
        fewest_zero = num_zeroes
        best = layer

print sum(1 for x in best if x == "1") * sum(1 for x in best if x == "2")
