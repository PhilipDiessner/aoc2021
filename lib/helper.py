import os


def load_input(file_path):
    with open(file_path, "r") as f:
        return f.read().rstrip()


def load_input_lines(file_path):
    with open(file_path, "r") as f:
        return f.readlines()


def load_intlist(file_path):
    return [int(y) for y in load_input(file_path).split(",")]


def load_input_int(file_path):
    return [int(x) for x in load_input_lines(file_path)]


def coord_dict_printready(d):
    xset = set([x[0] for x in d.keys()])
    yset = set([y[1] for y in d.keys()])
    xmin, xmax, ymin, ymax = min(xset), max(xset)+1, min(yset), max(yset)+1
    return ["".join(str(d[(x, y)]) for x in range(xmin, xmax)) for y in range(ymin, ymax)]


def coord_set_printready(d):
    xset = set([x[0] for x in d])
    yset = set([y[1] for y in d])
    xmin, xmax, ymin, ymax = min(xset), max(xset)+1, min(yset), max(yset)+1
    return ["".join(str("#" if (x, y) in d else ".") for x in range(xmin, xmax)) for y in range(ymin, ymax)]


def around(point, diag=False, include_point=False):
    if diag and include_point:
        return point-1j-1, point-1j, point-1j+1, point-1, point, point+1, point+1J-1, point+1J, point+1J+1
    elif diag:
        return point-1j-1, point-1j, point-1j+1, point-1, point+1, point+1J-1, point+1J, point+1J+1
    if include_point:
        return point-1j, point-1, point, point+1, point+1J
    else:
        return point+1, point-1, point+1J, point-1J
