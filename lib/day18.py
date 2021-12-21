import lib.helper as h


def get_input(data):
    return [eval(x) for x in h.load_input_lines(data)]


def add_snail(a, b):
    return [a]+[b]


def split(a):
    if isinstance(a, list):
        splitted, result = split(a[0])
        if splitted:
            return True, add_snail(result, a[1])
        else:
            splitted, result = split(a[1])
            return splitted, add_snail(a[0], result)
    else:
        if a < 10:
            return False, a
        else:
            return True, [b := a//2, a-b]


def exploded_to_right(new, a):
    if isinstance(a, list):
        return add_snail(exploded_to_right(new, a[0]), a[1])
    else:
        return a+new


def exploded_to_left(new, a):
    if isinstance(a, list):
        return add_snail(a[0], exploded_to_left(new, a[1]))
    else:
        return a+new


def explode(a, n=0):
    if n == 4 and isinstance(a, list):
        return 0, a[0], a[1], True
    else:
        if isinstance(a, list):
            new, left, right, exploded = explode(a[0], n+1)
            if exploded and right:
                return add_snail(new, exploded_to_right(right, a[1])), left, None, exploded
            elif exploded:
                return add_snail(new, a[1]), left, None, exploded
            else:
                other, left, right, exploded = explode(a[1], n+1)
                if exploded and left:
                    return add_snail(exploded_to_left(left, new), other), None, right, exploded
                else:
                    return add_snail(new, other), None, right, exploded
        else:
            return a, None, None, False


def reduce_snail(a):
    action = True
    while action:
        res, l, r, exploded = explode(a)
        if not exploded:
            action, res = split(a)
        a = res
    return a


def magnitude(a):
    return magnitude(a[0])*3+magnitude(a[1])*2 if isinstance(a, list) else a


def part1(inp):
    start = inp[0]
    for j in inp[1:]:
        #print(j)
        start = reduce_snail(add_snail(start, j))
    print(start)
    return magnitude(start)


def part2(inp):
    res = 0
    for i, first in enumerate(inp):
        for second in inp[:i]+inp[i+1:]:
            if res < (temp :=  magnitude(reduce_snail(add_snail(first, second)))):
                res = temp
    return res
