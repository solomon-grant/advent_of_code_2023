steps = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
}

with open("example.txt") as fp:
    grid = [[int(x) for x in line.strip()] for line in fp.readlines()]

height = len(grid)
width = len(grid[0])
fin = (height - 1, width - 1)
inf = sum(sum(line) for line in grid) + 1

known = {fin: 0}

def solve(row, col, path):
    print(row, col, path)
    if (row, col) == fin:
        return 0
    if row < 0 or row >= height or col < 0 or col >= width or (row, col) in visited or path[-4:] in ("UUUU", "DDDD", "LLLL", "RRRR"):
        return inf
    visited.add((row, col))
    dist = grid[row][col] + min(solve(row + r, col + c, path + d) for d, (r, c) in steps.items())
    visited.remove((row, col))
    return dist


print(min(solve(0, 1, "R"), solve(1, 0, "D")))
