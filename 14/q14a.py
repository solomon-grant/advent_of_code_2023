def tilt(grid):
    total = 0
    next_open = [0] * len(grid[0])
    for i, row in enumerate(grid):
        for j, elem in enumerate(row):
            if elem == "O":
                total += len(grid) - next_open[j]
                next_open[j] += 1
            if elem == "#":
                next_open[j] = i + 1
    print(total)


def solve(fname):
    with open(fname) as fp:
        grid = [line.strip() for line in fp.readlines()]
    tilt(grid)


solve("example.txt")
solve("input.txt")
