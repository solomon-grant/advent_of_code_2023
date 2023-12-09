import itertools


def diff(ints):
    if all(x == 0 for x in ints):
        return 0
    return ints[-1] + diff([y - x for x, y in itertools.pairwise(ints)])


def get_ints(line):
    return [int(x) for x in line.strip().split()]


with open("input.txt") as fp:
    print(sum(diff(get_ints(line)) for line in fp))
