import lib.helper as h
import networkx as nx
import igraph as ig


def get_input(data, with_nx=True):
    if with_nx:
        g = nx.Graph()
        for l in h.load_input_lines(data):
            g.add_edge(*l.rstrip().split("-"))
    else:
        g = ig.Graph()
        lines = [l.rstrip().split("-") for l in h.load_input_lines(data)]
        nodes = {k: v for v, k in enumerate(set([x for l in lines for x in l]))}
        print(nodes)
        g.add_vertices(len(nodes))
        for val, node in nodes.items():
            g.vs[node]["value"] = val
        for v1, v2 in lines:
            g.add_edge(nodes[v1], nodes[v2])
    return g


def walk_nx(n, g, way, twice):
    if (n == "start" and n in way) or ((n == n.lower()) and n in way and twice):
        return []
    elif n == "end":
        return [way]
    else:
        return [w for node in g[n] for w in walk_nx(node, g, way+[n], ((n == n.lower()) and n in way) or twice)]


def walk(n, g, way, twice):
    val = n["value"]
    if (val == "start" and n in way) or ((val == val.lower()) and n in way and twice):
        return []
    elif val == "end":
        return [way]
    else:
        return [w for node in g.vs(g.neighbors(n)) for w in walk(node, g, way+[n],
                                                          ((val == val.lower()) and n in way) or twice)]


def part1(inp):
    return len(walk_nx("start", inp, [], True))


def part2(inp):
    return len(walk_nx("start", inp, [], False))

