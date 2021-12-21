import lib.helper as h
from collections import Counter


def get_input(data):
    return [[list(map(int, y.split(","))) for y in x.split(" -> ")] for x in h.load_input_lines(data)]


def analyse(x1, y1, x2, y2, points, diag=False):
    if x1 == x2:
        for y in range(y1, y2+1) if y2 > y1 else range(y2, y1+1):
            points[(x1, y)] += 1
    elif y1 == y2:
        for x in range(x1, x2+1) if x2 > x1 else range(x2, x1+1):
            points[(x, y1)] += 1
    elif diag and abs(x2-x1) == abs(y2-y1):
        xrange = range(x1, x2+1) if x2 > x1 else range(x1, x2-1, -1)
        yrange = range(y1, y2+1) if y2 > y1 else range(y1, y2-1, -1)
        for x, y in zip(xrange, yrange):
            points[(x, y)] += 1


def part1(inp):
    points = Counter()
    for (x1, y1), (x2, y2) in inp:
        analyse(x1, y1, x2, y2, points)
    return sum([1 for v in points.values() if v>1])


def part2(inp):
    points = Counter()
    for (x1, y1), (x2, y2) in inp:
        analyse(x1, y1, x2, y2, points, diag=True)
    #for l in h.coord_dict_printready(points):
    #    print(l.replace("0", "."))
    return sum([1 for v in points.values() if v>1])

