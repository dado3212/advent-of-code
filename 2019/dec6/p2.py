real = open("./input.txt", "r")
sample = open("./sample2.txt", "r")

def num_moves(vs):
    # Calculate the graph
    orbiters = set()
    orbiteds = set()
    planet_to_orbiter = {}
    for x in vs:
        orbit = x[:-1].split(")")
        orbited = orbit[0]
        orbiter = orbit[1]
        orbiteds.add(orbited)
        orbiters.add(orbiter)
        if orbited not in planet_to_orbiter:
            planet_to_orbiter[orbited] = set()
        if orbiter not in planet_to_orbiter:
            planet_to_orbiter[orbiter] = set()
        planet_to_orbiter[orbited].add(orbiter)

    # Find the starting position
    seeds = orbiteds.difference(orbiters)
    seed = seeds.pop()

    # Shortest path from seed, and then connect them (take advantage of graph shape)
    path_to_you = find_path(seed, "YOU", planet_to_orbiter, [])
    path_to_san = find_path(seed, "SAN", planet_to_orbiter, [])
    index = 0
    while path_to_san[index] == path_to_you[index]:
        index += 1
    return len(path_to_you) + len(path_to_san) - 2 * index - 2


def find_path(seed, find, planet_to_orbiter, path):
    if seed == find:
        path.append(find)
        return path
    else:
        if seed in planet_to_orbiter:
            best = False
            for orbiter in planet_to_orbiter[seed]:
                f = path[:]
                f.append(seed)
                a = find_path(orbiter, find, planet_to_orbiter, f)
                if a != False:
                    if best == False or len(best) > len(a):
                        best = a
            return best
        else:
            return False

print num_moves(sample.readlines())
print num_moves(real.readlines())
