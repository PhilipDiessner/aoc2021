import lib.helper as h


def get_input(data):
    return [[int(y) for y in x[2:].split("..")]for x in h.load_input(data)[13:].split(", ")]


def part1(inp):
    hmax = {}
    for vx in range(300):
        for vy in range(-300,400):
            v = [vx, vy]
            h = 0
            s = [0, 0]
            while True:
                s[0], v[0] = s[0]+v[0], v[0]-1 if v[0] > 0 else 0
                s[1], v[1] = s[1]+v[1], v[1]-1
                h = max(h, s[1])
                if inp[0][0]<=s[0]<=inp[0][1] and inp[1][0]<=s[1]<=inp[1][1]:
                    hmax[(vx, vy)] = h
                    break
                elif s[0]>inp[0][1] or s[1]<inp[1][0]:
                    break
    return max(hmax.values()), len(hmax)


def part2(inp):
    return 0
