import importlib
from time import time


def main(day, sample=False, printer=False):
    i = importlib.import_module("lib." + day)

    datapath = "./data/" + day + ("_sample.txt" if sample else "_input.txt")
    start = time()
    inp = i.get_input(datapath)
    print("Setup Time:", time()-start)
    start = time()

    print("Part 1:", i.part1(inp), "Time:", time()-start)
    start = time()

    print("Part 2:", i.part2(inp), "Time:", time()-start)


if __name__ == '__main__':
    main('day20', sample=False)

