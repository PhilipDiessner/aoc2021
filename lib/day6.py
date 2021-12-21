import lib.helper as h
import math
from collections import deque, Counter


comb = {}
def combination(n, r):
    if (n, r) in comb:
        return comb[(n, r)]
    comb[(n, r)] = (res := int((math.factorial(n)) // ((math.factorial(r)) * math.factorial(n - r))))
    return res


def spawn_children(counter, start, end):
    delta = end - start - counter - 1
    nc = 1 + (delta // 7) if delta > -1 else 0
    return 1 + sum([spawn_children(8, start + counter + 7 * c + 1, end) for c in range(nc)])


def analytical(start, end):
    k1, k2 = 7, 9
    delta = end - start
    n1 = delta // k1

    def split(i, n):
        return combination(n, i) if k2 * i + k1 * (n - i) <= delta else split(i - 1, n - 1)
    return sum(split(j, n1) for j in range(n1+1))


def get_input(data):
    return h.load_intlist(data)


def part1(inp):
    old = inp
    for i in range(8):
        new = []
        add = []
        for elem in old:
            new.append(elem - 1 if elem > 0 else 6)
            if elem == 0:
                add.append(8)
        new.extend(add)
        old = new
    return len(old)


def part2(inp):
    groups = deque([sum(1 for x in inp if x == i) for i in range(9)])
    for _ in range(256):
        groups.append(groups.popleft())
        groups[6] += groups[-1]
    return sum(groups)
    birth = Counter(inp)
    print(birth)
    for day in range(256):
        birth[day] += birth[day-7] + birth[day-9]
    return sum(birth.values())+len(inp)
    # print([analytical(x-6, 256) for x in inp])
    return sum([analytical(x-6, 256) for x in inp])
