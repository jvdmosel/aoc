from itertools import permutations

cities = set()
E = {}

with open("input", "r") as reader:
    for line in reader:
        a, _, b, _, distance = line.split(" ")
        distance = int(distance.strip())
        cities.add(a)
        cities.add(b)
        if a not in E.keys():
            E[a] = {}
        if b not in E.keys():
            E[b] = {}
        E[a][b] = distance
        E[b][a] = distance

longest_route = 0
for perm in permutations(cities):
    route = 0
    for i in range(len(perm)-1):
        route += E[perm[i]][perm[i+1]]
    if route > longest_route:
        longest_route = route
print(longest_route)
