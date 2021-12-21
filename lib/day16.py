import lib.helper as h
from functools import reduce
import operator


class Packet:
    def __init__(self, version, typ):
        self.version = version
        self.typ = typ
        self.length_ID = None
        self.children = []
        self.val = None

    def interpret(self):
        val_children = (x.interpret() for x in self.children)
        if self.typ == 4:
            return self.val
        elif self.typ == 0:
            return sum(val_children)
        elif self.typ == 1:
            return reduce(operator.mul, val_children, 1)
        elif self.typ == 2:
            return min(val_children)
        elif self.typ == 3:
            return max(val_children)
        elif self.typ == 5:
            return next(val_children) > next(val_children)
        elif self.typ == 6:
            return next(val_children) < next(val_children)
        elif self.typ == 7:
            return next(val_children) == next(val_children)


def to_binary(in_string):
    return "".join(format(int(x, 16), '04b') for x in in_string)


def get_input(data):
    return to_binary(h.load_input(data))


def parse(inp):
    test = inp[:]
    packet = Packet(int(test[:3], 2), int(test[3:6], 2))
    test = test[6:]
    if packet.typ == 4:
        val = ""
        while test[0] == "1":
            val += test[1:5]
            test = test[5:]
        packet.val = int(val+test[1:5], 2)
        #print("val", packet.val)
        return packet, test[5:]
    else:
        packet.length_ID = test[0]
        if test[0] == "0":
            nbits = int(test[1:16], 2)
            rest = test[16:16+nbits]
            #print(nbits,test[16:16+nbits], test[16+nbits:])
            while rest:
                p, rest = parse(rest)
                packet.children.append(p)
            return packet, test[16+nbits:]
        else:
            npack = int(test[1:12], 2)
            rest = test[12:]
            #print(npack, test[12:])
            for _ in range(npack):
                p, rest = parse(rest)
                packet.children.append(p)
            return packet, rest


def add_versions(p):
    return p.version + sum(add_versions(c) for c in p.children)


def part1(inp):
    packet, _ = parse(inp)
    return add_versions(packet)


def part2(inp):
    packet, _ = parse(inp)
    return int(packet.interpret())
