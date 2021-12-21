import lib.helper as h


def get_input(data):
    return [[int(y) for y in x[:-1]] for x in h.load_input_lines(data)]


def dominant_bit(pool, pos):
    return int(2*sum(x[pos] for x in pool)/len(pool))


def to_number(gamma):
    return int("".join(gamma), 2)


def filter_pool(pool, pos, inverse=0):
    if len(pool) > 1:
        digit = (dominant_bit(pool, pos) + inverse) & 1
        return [num for num in pool if num[pos] == digit]
    else:
        return pool


def part1(inp):
    gamma = to_number([str(dominant_bit(inp, l)) for l in range(len(inp[0]))])
    return gamma*((2**len(inp[0])-1)-gamma)


def part2(inp):
    o2pool = inp[:]
    co2pool = inp[:]
    for l in range(len(inp[0])):
        o2pool = filter_pool(o2pool, l)
        co2pool = filter_pool(co2pool, l, 1)
    o2 = to_number([str(x) for x in o2pool[0]])
    co2 = to_number([str(x) for x in co2pool[0]])
    return o2*co2
