import itertools


def tilt(grid):
    next_open = [0] * len(grid[0])
    for i, row in enumerate(grid):
        for j, elem in enumerate(row):
            if elem == "O":
                grid[i][j] = "."
                grid[next_open[j]][j] = "O"
                next_open[j] += 1
            if elem == "#":
                next_open[j] = i + 1


def cycle(grid):
    for _ in "NWSE":
        tilt(grid)
        grid = [list(col) for col in zip(*reversed(grid))]
    return grid


def get_key(grid):
    return tuple(i for i, elem in enumerate(itertools.chain(*grid)) if elem == "O")


def solve(fname):
    with open(fname) as fp:
        grid = [list(line.strip()) for line in fp.readlines()]
    cache = set()
    count = 0
    key = get_key(grid)
    while key not in cache:
        cache.add(key)
        grid = cycle(grid)
        key = get_key(grid)
        count += 1

    grid = cycle(grid)
    next_key = get_key(grid)
    cycle_length = 1
    while next_key != key:
        grid = cycle(grid)
        next_key = tuple(i for i, elem in enumerate(itertools.chain(*grid)) if elem == "O")
        cycle_length += 1

    for i in range((1_000_000_000 - (count - cycle_length)) % cycle_length):
        grid = cycle(grid)

    total = 0
    for i, row in enumerate(grid):
        total += (len(grid) - i) * row.count("O")
    print(total)


solve("example.txt")
solve("input.txt")
