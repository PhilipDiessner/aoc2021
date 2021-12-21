import lib.helper as h
from collections import Counter
from itertools import combinations

def distance(a, b):
    return a[0] - b[0], a[1] - b[1], a[2] - b[2]


class Scanner:
    def __init__(self, text):
        lines = text.split("\n")
        self.id = int(lines[0][12:-4])
        self.beacons = [tuple(int(y) for y in x.split(",")) for x in lines[1:]]
        self.distances = {}
        self.directed = {}
        self.neighbors = []
        self.new_beacons = set()
        self.scanners = {}
        for i, a in enumerate(self.beacons):
            for j, b in enumerate(self.beacons[i+1:], i+1):
                d = (a[0]-b[0], a[1]-b[1], a[2]-b[2])
                self.directed[(i, j)] = d
                self.distances[(i, j)] = sum(abs(x)**2 for x in d)
        self.pairings = {v: k for k, v in self.distances.items()}

    def find_matches(self, exclude=[]):
        for scanner, dists in self.neighbors:
            if scanner.id in exclude:
                continue
            scanner.find_matches(exclude+[self.id])
            matches = {}
            for i in (a := set(y for x in dists for y in self.pairings[x])):
                d = set([y for x, y in self.distances.items()
                         if (i == x[0]) or (i == x[1])]).intersection(dists)
                matches[i] = Counter(x for z in d for x in scanner.pairings[z]).most_common(1)[0][0]
            d1 = scanner.directed[scanner.pairings[dists[12]]]
            d0 = self.directed[self.pairings[dists[12]]]
            ordering = [[abs(y) for y in d1].index(x) for x in [abs(y) for y in d0]]
            ordering = [(ordering[i], x//d1[ordering[i]]) for i, x in enumerate(d0)]
            off_set = []
            for x, y in matches.items():
                off_set.append(list(zip(*[(self.beacons[x][a]+scanner.beacons[y][i]*j,
                                           self.beacons[x][a]-scanner.beacons[y][i]*j)
                            for a, (i, j) in enumerate(ordering)])))
            transport = (off_set[0][0], 1) if off_set[0][0]==off_set[1][0] \
                                              and off_set[0][0]==off_set[2][0] \
                else (off_set[0][1], -1)
            for beacon in set(scanner.beacons).union(scanner.new_beacons):
                self.new_beacons.add(tuple([transport[0][a]-transport[1]*beacon[i]*j
                                               for a, (i, j) in enumerate(ordering)]))
            self.scanners[scanner.id] = transport[0]
            for k,s in scanner.scanners.items():
                self.scanners[k] = tuple([transport[0][a]-transport[1]*s[i]*j
                                               for a, (i, j) in enumerate(ordering)])
        #print(len(set(self.beacons+self.new_beacons)))


def get_input(data):
    scanners = h.load_input(data).split("\n\n")
    return [Scanner(x) for x in scanners]


def part1(inp):
    print(range(len(inp[0].beacons)))
    res = set()
    beacons = set((i, j) for i, scanner in enumerate(inp) for j, _ in enumerate(scanner.beacons))
    print(len(beacons))
    for i, scanner in enumerate(inp):
        dist = set(scanner.distances.values())
        res.update(dist)
        for j, scanner1 in enumerate(inp[i+1:], i+1):
            dist1 = set(scanner1.distances.values())
            inter = dist1.intersection(dist)
            if len(inter) >= 66:
                scanner.neighbors.append((scanner1, list(inter)))
                scanner1.neighbors.append((scanner, list(inter)))
    inp[0].find_matches()
    print("almost done")
    return len(set(inp[0].beacons).union(inp[0].new_beacons)), \
           max([sum(abs(i) for i in distance(*x)) for x in combinations(inp[0].scanners.values(),2)])


def part2(inp):
    return 0
