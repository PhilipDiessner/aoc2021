import lib.helper as h
from collections import defaultdict, Counter


def get_input(data):
    inp = h.load_input_lines(data)
    mapping = defaultdict(lambda: 0)
    for y, line in enumerate(inp[2:]):
        for x, c in enumerate(line[:-1]):
            if c == '#':
                mapping[x+1J*y] = 1
    return inp[0], mapping


def step(algo, mapping, n):
    new = defaultdict(lambda: 0) if n % 2 == 1 else defaultdict(lambda: 1)
    xset = set([int(x.real) for x in mapping])
    yset = set([int(y.imag) for y in mapping])
    xmin, xmax, ymin, ymax = min(xset), max(xset)+1, min(yset), max(yset)+1
    for p in (x+1J*y for x in range(xmin-1, xmax+1) for y in range(ymin-1, ymax+1)):
        if n % 2 == 1:
            if algo[int("".join([str(mapping[x]) for x in h.around(p, True, True)]), 2)] == '#':
                new[p] = 1
        else:
            if algo[int("".join([str(mapping[x]) for x in h.around(p, True, True)]), 2)] == '.':
                new[p] = 0
    return new


def part1(inp):
    algo, mapping = inp
    for i in range(2):
        mapping = step(algo, mapping, i)
    return len(mapping)


def part2(inp):
    algo, mapping = inp
    for i in range(50):
        mapping = step(algo, mapping, i)
    return len(mapping)
