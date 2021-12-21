import lib.helper as h


def get_input(data):
    return [[x.split() for x in line.split(" | ")] for line in h.load_input_lines(data)]


def sorted_string(inp):
    return "".join(sorted(inp))


def reduce_unkown(triple, steps, matches):
    for i, step in steps:
        matches[i] = triple[[sorted_string(set(matches[step]+x))
                             for x in triple].index(matches[8])]
        triple.remove(matches[i])


def get_pos(pattern):
    combs = set(map(sorted_string,pattern))
    out = {1: [x for x in combs if len(x) == 2][0], 4: [x for x in combs if len(x) == 4][0],
           7: [x for x in combs if len(x) == 3][0], 8: [x for x in combs if len(x) == 7][0]}
    twothreefive = [x for x in combs if len(x) == 5]
    zerosixnine = [x for x in combs if len(x) == 6]
    reduce_unkown(zerosixnine, [(6, 1), (0, 4)], out)
    out[9] = zerosixnine[0]
    reduce_unkown(twothreefive, [(2, 4), (5, 2)], out)
    out[3] = twothreefive[0]
    return {v: k for k, v in out.items()}


def part1(inp):
    pattern, values = zip(*inp)
    return sum(1 for vals in values for x in vals if len(x) in (2,3,4,7))


def part2(inp):
    res = 0
    for pattern, values in inp:
        match = get_pos(pattern)
        res += int("".join(str(match["".join(sorted(x))]) for x in values))
    return res
