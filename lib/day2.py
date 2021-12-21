import lib.helper as h


def get_input(data):
    return [x.split(" ") for x in h.load_input_lines(data)]


def part1(inp):
    coord = 0
    functions = {"forward": lambda x, y: x+y, "down": lambda x, y: x+1j*y, "up": lambda x, y: x-1j*y}
    for instr, number in inp:
        coord = functions[instr](coord, int(number))
    return int(coord.real*coord.imag)


def part2(inp):
    coord = 0
    aim = 0
    functions = {"forward": lambda x, y, z: x+y*(1+1j*z), "down": lambda x, y, z: z+y, "up": lambda x, y, z: z-y}
    for instr, number in inp:
        coord = functions[instr](coord, int(number), aim)
    return int(coord.real*coord.imag)
