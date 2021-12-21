import lib.helper as h


def get_input(data):
    return h.load_input_int(data)


def slide(inp, step=1):
    return sum([y > x for x, y in zip(inp[:-step], inp[step:])])


def part1(inp):
    return slide(inp)


def part2(inp):
    return slide(inp, 3)
