import heapq as hq
import math
from functools import total_ordering, partial
import lib.helper as h
import networkx as nx


@total_ordering
class Way:
    def __init__(self, point, cost=None):
        self.current = point
        self.cost = cost if cost else 0

    def __eq__(self, other):
        return self.cost == other.cost

    def __lt__(self, other):
        return self.cost < other.cost


def get_input(data):
    # g = nx.Graph()
    # lines = h.load_input_lines(data)
    # for y, line in enumerate(lines):
    #     for x, c in enumerate(line[:-1]):
    #         g.add_node(x+10*y, value=int(c), fired=False)
    #         for x1, y1 in [(-1, 0), (-1, -1), (0, -1), (1, -1)]:
    #             if (0 <= x+x1 <= 9) and (0 <= y+y1 <= 9):
    #                 g.add_edge(x+10*y, x+x1+10*(y+y1))
    # return g
    return {x+1J*y: int(char) for y, line in enumerate(h.load_input_lines(data))
                              for x, char in enumerate(line[:-1])}


def fullinp(point, inp):
    x, y = point.real % 100, point.imag % 100
    x_off, y_off = point.real // 100, point.imag // 100
    return int((inp[x+1J*y]-1+x_off+y_off) % 9 + 1)


def djik(start, end, g):
    heap = []
    costs = {start: 0}
    prev = {}
    hq.heappush(heap, Way(start))
    for point in g:
        if point != 0j:
            costs[point] = math.inf
            hq.heappush(heap, Way(point, cost=math.inf))
    while end != (point := hq.heappop(heap)).current:
        for p in h.around(point.current):
            if (point.current in prev and p == prev[point.current]) or p not in g:
                continue
            alt = point.cost + g[p]
            if alt < costs[p]:
                costs[p] = alt
                prev[p] = point.current
                hq.heappush(heap, Way(p, cost=alt))
    return point.cost


def part1(inp):
    return djik(0j, 99+99j, inp)


def part2(inp):
    new_inp = {}
    getter = partial(fullinp, inp=inp)
    for y in range(500):
        for x in range(500):
            val = x+1J*y
            new_inp[val] = getter(val)

    return djik(0j, 499+499j, new_inp)
