import lib.helper as h
from collections import defaultdict
from functools import reduce


def get_input(data):
    return defaultdict(lambda: 9,
                       {x+1J*y: int(char) for y, line in enumerate(h.load_input_lines(data))
                        for x, char in enumerate(line[:-1])})


def surround_in_basin(point, inp, basin):
    if inp[point] < 9 and point not in basin:
        basin.add(point)
        [surround_in_basin(p, inp, basin) for p in h.around(point)]


def part1(inp):
    res = 0
    for x in range(100):
        for y in range(100):
            point = x+1J*y
            if all([inp[p] > (val := inp[point]) for p in h.around(point)]):
                res += 1 + val
    return res


def part2(inp):
    final = []
    for x in range(100):
        for y in range(100):
            point = x+1J*y
            if all([inp[p] > inp[point] for p in h.around(point)]):
                basin = set()
                surround_in_basin(point, inp, basin)
                final.append(len(basin))
    return reduce(lambda a,b: a*b, sorted(final)[-3:])
