import lib.helper as h


def get_input(data):
    return h.load_input_lines(data)


def analyze_line(line):
    opening = []
    for c in line[:-1]:
        if c in "<({[":
            opening.append(c)
        else:
            d = opening.pop()
            if not any((d == '(' and c == ')', d == '<' and c == '>',
                   d == '[' and c == ']', d == '{' and c == '}')):
                return score1(c)
    score = 0
    for c in opening[::-1]:
        score = score2(c, score)
    return -score


def score1(char):
    if char == ')':
        return 3
    elif char == ']':
        return 57
    elif char == '}':
        return 1197
    elif char == '>':
        return 25137
    else:
        return 0


def score2(char, init=0):
    for i, d in enumerate("([{<"):
        if char == d:
            return init*5+(i+1)


def part1(inp):
    return sum([x for x in map(analyze_line, inp) if x > 0])


def part2(inp):
    res = sorted([-x for x in map(analyze_line, inp) if x < 0])
    print(res)
    return res[len(res)//2]
