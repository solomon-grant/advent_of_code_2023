import math


class StepIterator:
    def __init__(self, steps_string):
        self.i = 0
        self.steps = steps_string

    def __iter__(self):
        return self

    def __next__(self):
        step = self.steps[self.i]
        self.i = (self.i + 1) % len(self.steps)
        return step


def make_map(map_data):
    new_map = dict()
    for line in map_data:
        node = line[0:3]
        left = line[7:10]
        right = line[12:15]
        new_map[node] = {"L": left, "R": right}
    return new_map


def traverse(m, s):
    starts = [node for node in m if node.endswith("A")]
    cycles = [0 for node in starts]
    for i, start in enumerate(starts):
        curr = start
        for step in s:
            curr = m[curr][step]
            cycles[i] += 1
            if curr.endswith("Z"):
                break
    return cycles


def solve(fname):
    with open(fname) as fp:
        steps_string = fp.readline().strip()
        fp.readline()
        map_data = fp.readlines()
    cycles = traverse(make_map(map_data), StepIterator(steps_string))
    return math.lcm(*cycles)


if __name__ == "__main__":
    print(solve("example3.txt"))
    print(solve("input.txt"))
