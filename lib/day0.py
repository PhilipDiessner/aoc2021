import math
import numpy as np
import lib.helper as h


class Tile:
    def __init__(self, lines):
        self.name = lines[0][5:-1]
        self.content = np.asarray([[y for y in x[1:-1]] for x in lines[2:-1]])
        self.borders = ["".join([x[0] for x in lines[1:]]), lines[1],
                        "".join([x[-1] for x in lines[1:]]), lines[-1]]
        self.edges = [None]*4
        self.orientation = 1+1j

    def all_border(self):
        return self.borders+[x[::-1] for x in self.borders]

    def rotate_left(self):
        self.borders = self.rotate_border_left(self.borders)
        self.edges = self.edges[1:]+[self.edges[0]]
        self.content = np.rot90(self.content)

    def flip_tb(self):
        self.borders = self.flip_border_tb(self.borders)
        self.edges[1], self.edges[3] = self.edges[3], self.edges[1]
        self.content = np.flipud(self.content)

    @staticmethod
    def rotate_border_left(border):
        return [border[1][::-1], border[2], border[3][::-1], border[0]]

    @staticmethod
    def flip_border_tb(border):
        return [border[0][::-1], border[3], border[2][::-1], border[1]]


def get_input(data):
    return [Tile(x.split("\n")) for x in h.load_input(data).split("\n\n")][:-1]


def part1(inp):
    borders = []
    for border in [tile.all_border() for tile in inp]:
        borders.extend(border)
    res = 1
    print(len(inp))
    for tile in inp:
        if sum([borders.count(border) for border in tile.borders]) == 6:
            res *= int(tile.name)
    return res


def scan(seed, stack, direction, steps):
    for _ in range(steps):
        active = seed[-1].borders[direction]
        for tile in stack:
            if active in tile.all_border():
                for _ in range(2):
                    for _ in range(4):
                        if active == tile.borders[(direction+2) % 4]:
                            break
                        else:
                            tile.rotate_left()
                    if active != tile.borders[(direction+2) % 4]:
                        tile.flip_tb()
                seed.append(tile)
                break
        stack.remove(tile)


def part2(inp):
    borders = []
    corners = []
    outer = []
    inner = []
    n = len(inp)
    side = int(math.sqrt(n))
    for border in [tile.all_border() for tile in inp]:
        borders.extend(border)
    for tile in inp:
        tile.edges = [borders.count(border) for border in tile.borders]
        if sum(tile.edges) == 6:
            corners.append(tile)
        elif sum(tile.edges) == 7:
            outer.append(tile)
        else:
            inner.append(tile)
    border = [corners[0]]
    while True:
        if border[0].edges[:2] == [1, 1]:
            break
        else:
            border[0].rotate_left()
    scan(border, outer, 3, side-2)
    scan(border, corners[1:], 3, 1)
    remainder = outer+inner+corners
    border = [[x] for x in border]
    for x in border:
        scan(x, remainder, 2, side-1)
    image = [[y.content for y in x] for x in border]
    image = np.vstack([np.hstack(x) for x in image])
    snake = ((1,0), (2,1), (2,4), (1,5), (1,6), (2,7), (2,10), (1,11), (1,12), (2,13), (2,16),(1,17),(1,18),(0,18),(1,19))
    count = [0]*8
    images = [image, np.rot90(image), np.rot90(image, 2), np.rot90(image, 3)]
    images = images + [np.flipud(img) for img in images]
    for i, img in enumerate(images):
        for y in range(image.shape[0]-2):
            for x in range(image.shape[1]-19):
                count[i] += all([img[y+yi][x+xi] == '#' for yi, xi in snake])
    print(count)
    print(sum(x.count('#') for x in image.tolist())-sum(count)*len(snake))
    return 0
