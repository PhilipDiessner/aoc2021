import lib.helper as h
import networkx as nx
import igraph as ig


def get_input(data, with_nx=False):
    if with_nx:
        g = nx.Graph()
        lines = h.load_input_lines(data)
        for y, line in enumerate(lines):
            for x, c in enumerate(line[:-1]):
                g.add_node(x+10*y, value=int(c), fired=False)
                for x1, y1 in [(-1, 0), (-1, -1), (0, -1), (1, -1)]:
                    if (0 <= x+x1 <= 9) and (0 <= y+y1 <= 9):
                        g.add_edge(x+10*y, x+x1+10*(y+y1))
    else:
        g = ig.Graph()
        g.add_vertices(100)
        lines = h.load_input_lines(data)
        for y, line in enumerate(lines):
            for x, c in enumerate(line[:-1]):
                g.vs[x+10*y]["value"] = int(c)
                for x1, y1 in [(-1, 0), (-1, -1), (0, -1), (1, -1)]:
                    if (0 <= x+x1 <= 9) and (0 <= y+y1 <= 9):
                        g.add_edge(x+10*y, x+x1+10*(y+y1))
    return g


def fire(v, g):
    if v["value"] > 9 and not v["fired"]:
        v["fired"] = True
        res = 1
        for n in g.neighbors(v):
            g.vs[n]["value"] += 1
            res += fire(g.vs[n], g)
        return res
    else:
        return 0


def fire_nx(v, g):
    if g.nodes[v]["value"] > 9 and not g.nodes[v]["fired"]:
        g.nodes[v]["fired"] = True
        res = 1
        for n in g[v]:
            g.nodes[n]["value"] += 1
            res += fire_nx(n, g)
        return res
    else:
        return 0


def loop(g):
    fired = 0
    for v in g.vs:
        if v["value"] > 9:
            v["value"] = 1
        else:
            v["value"] += 1
        v["fired"] = False
    for v in g.vs:
        fired += fire(v, g)
    return fired


def loop_nx(g):
    fired = 0
    for v in g.nodes:
        if g.nodes[v]["value"] > 9:
            g.nodes[v]["value"] = 1
        else:
            g.nodes[v]["value"] += 1
        g.nodes[v]["fired"] = False
    for v in g.nodes:
        fired += fire_nx(v, g)
    return fired


def part1(inp):
    return sum(loop_nx(inp) for _ in range(100))


def part2(inp):
    fired = 0
    step = 100
    while fired < 100:
        step += 1
        fired = loop_nx(inp)
    return step

