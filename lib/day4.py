import lib.helper as h


class Bingo:
    def __init__(self, data):
        self.d = {x: [i, j, 1] for j, y in enumerate(data) for i, x in enumerate(y.split())}
        self.rows = [0]*5
        self.columns = [0]*5
        self.bingo = False

    def drop_number(self, n):
        if n in self.d:
            self.d[n][-1] = 0
            self.columns[self.d[n][0]] += 1
            self.rows[self.d[n][1]] += 1

    def check_bingo(self):
        return self.bingo or self.check_bingo_helper()

    def check_bingo_helper(self):
        for line in self.rows+self.columns:
            if line == 5:
                self.bingo = True
                return True
        return False

    def score(self, n):
        return int(n)*sum(int(k)*v[-1] for k, v in self.d.items())


def get_input(data):
    inp = h.load_input(data).split("\n\n")
    return [x for x in inp[0].split(",")], [Bingo(x.split("\n")) for x in inp[1:]]


def part1(inp):
    for bingo in inp[1]:
        for number in inp[0]:
            bingo.drop_number(number)
            if bingo.check_bingo():
                return bingo.score(number)
    raise ValueError


def part2(inp):
    result = None
    for i, number in enumerate(inp[0]):
        for bingo in inp[1]:
            if not bingo.bingo:
                bingo.drop_number(number)
                if bingo.check_bingo():
                    result = bingo.score(number)
    return result
