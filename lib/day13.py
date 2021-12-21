import lib.helper as h


def get_input(data):
    points = set()
    folds = []
    for line in h.load_input_lines(data):
        if line=='\n':
            continue
        elif line[:4] == "fold":
           split = line[11:].split("=")
           folds.append([split[0], int(split[1])])
        else:
            points.add(tuple([int(x) for x in line.split(",")]))
    return points, folds


def iter_points(points, fold):
        new = set()
        for point in points:
            if fold[0] =='x' and point[0]>fold[1]:
                new.add((2*fold[1]-point[0], point[1]))
            elif fold[0] =='y' and point[1]>fold[1]:
                new.add((point[0], 2*fold[1]-point[1]))
            else:
                new.add(point)
        points = new
        return points


def part1(inp):
    points, folds = inp
    for fold in folds[:1]:
        points = iter_points(points, fold)
    return len(points)


def part2(inp):
    points, folds = inp
    for fold in folds:
        points = iter_points(points, fold)
    for l in h.coord_set_printready(points):
        print(l)
    return len(points)
