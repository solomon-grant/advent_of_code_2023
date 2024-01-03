class Coord:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __eq__(self, other):
        return (self.row, self.col) == (other.row, other.col)

    def __ne__(self, other):
        return (self.row, self.col) != (other.row, other.col)

    def __lt__(self, other):
        return (self.row, self.col) < (other.row, other.col)

    def __add__(self, other):
        return Coord(self.row + other.row, self.col + other.col)

    def __sub__(self, other):
        return Coord(self.row - other.row, self.col - other.col)

    def __hash__(self):
        return self.row // width + self.col % width

    def __repr__(self):
        return str((self.row, self.col))


up = Coord(-1, 0)
down = Coord(1, 0)
left = Coord(0, -1)
right = Coord(0, 1)

with open("input.txt") as fp:
    grid = [line.strip() for line in fp.readlines()]
width = len(grid[0])
height = len(grid)
inf = width * height + 1
start = Coord(0, grid[0].find("."))
end = Coord(len(grid) - 1, grid[-1].find("."))


def adjacent(coord: Coord, prev: Coord | None):
    adj = []
    for d in (up, down, left, right):
        n = coord + d
        if n.row < 0 or n.row >= height or n.col < 0 or n.col >= width or (prev is not None and n == prev):
            continue
        sym = grid[n.row][n.col]
        if sym == "#":
            continue
        adj.append(n)
    return adj


V = {start, end}
for i in range(height):
    for j in range(width):
        sym = grid[i][j]
        if sym == "#":
            continue
        c = Coord(i, j)
        adj = adjacent(c, None)
        if len(adj) > 2:
            V.add(c)


def walk_from(coord: Coord):
    adj = dict()
    for n in adjacent(coord, None):
        prev = coord
        steps = 1
        while n not in V:
            n, prev = adjacent(n, prev)[0], n
            steps += 1
        adj[n] = steps
    return adj


G = {v: walk_from(v) for v in V}
seen = set()


def walk(coord: Coord):
    if coord == end:
        return 0
    if coord in seen:
        return -inf

    seen.add(coord)
    steps = max(d + walk(n) for n, d in G[coord].items())
    seen.remove(coord)
    return steps


total = walk(start)
print(total)
