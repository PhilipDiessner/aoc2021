import lib.helper as h
from collections import Counter, defaultdict
import math


def get_input(data):
    return h.load_intlist(data)


def median(inp):
    l = sorted(inp)
    return (l[len(l)//2] + l[int(0.5+len(l))//2])//2

def fuel1(x0, inp):
    return sum([abs(x0-x)*i for x, i in inp.items()])


def dev_fuel1(x0, inp):
    return sum([(x0-x)*i/abs(x-x0) if x0!=x else 0 for x, i in inp.items()])


def fuel2(x0, inp):
    return sum([(d:=abs(x0-x))*(d+1)*i//2 for x, i in inp.items()])


def part1(inp):
    buckets = Counter(inp)
    s = sum(buckets.values())
    mean = round(sum([x*i for i, x in buckets.items()])/s)
    std = round(math.sqrt(sum([(x*i/s-mean)**2 for i, x in buckets.items()])/s))
    return min([fuel1(x, buckets) for x in range(mean-std, mean+std)]), std, mean, median(inp), fuel1(median(inp), buckets)


def part2(inp):
    buckets = Counter(inp)
    s = sum(buckets.values())
    mean = round(sum([x*i for i, x in buckets.items()])/s)
    std = round(math.sqrt(sum([(x*i/s-mean)**2 for i, x in buckets.items()])/s))
    spent = [fuel2(x, buckets) for x in range(mean-3, mean+3)]
    print(fuel2(mean+median(inp), buckets))
    return min(spent), min(inp), max(inp)
