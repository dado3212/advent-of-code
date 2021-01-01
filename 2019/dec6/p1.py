real = open("./input.txt", "r")
sample = open("./sample.txt", "r")

def checksum(vs):
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

    # Breadth first search with count
    return recursive_count(seed, planet_to_orbiter, 0)

def recursive_count(planet, planet_to_orbiter, count):
    if planet not in planet_to_orbiter:
        return count
    else:
        total = 0
        for orbiter in planet_to_orbiter[planet]:
            total += recursive_count(orbiter, planet_to_orbiter, count + 1)
        return total + count
    total = 0

print checksum(sample.readlines())
print checksum(real.readlines())
