import lib.helper as h
from collections import Counter


def get_input(data):
    lines = h.load_input_lines(data)
    return lines[0].rstrip(), {k: v for k,v in [tuple(x.rstrip().split(" -> ")) for x in lines[2:]]}


def step1(template, rules):
    new = ""
    for pos, char in enumerate(template[:-1]):
        new += char + rules.get(template[pos:pos+2])
    new += template[-1]
    return new


def step2(pairs, rules):
    new = Counter()
    for pair, count in pairs.items():
        add = rules.get(pair)
        new.update(Counter({pair[0]+add: count, add+pair[1]: count}))
    return new


def part1(inp):
    template, rules = inp
    for i in range(10):
        template = step1(template, rules)
    c = Counter(template)
    return c.get(max(set(template), key=c.get)) - c.get(min(set(template), key=c.get))


def part2(inp):
    template, rules = inp
    pairs = Counter([template[pos:pos+2] for pos, char in enumerate(template[:-1])])
    for i in range(40):
        pairs = step2(pairs, rules)
    c = sum([Counter({x: v for x in k}) if k[0] != k[1] else Counter({k[0]: 2*v}) for k, v in pairs.items()],
            Counter([template[0], template[-1]]))

    return (c.get(max(set(c), key=c.get)) - c.get(min(set(c), key=c.get)))//2
