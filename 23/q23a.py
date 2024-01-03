with open("input.txt") as fp:
    grid = [line.strip() for line in fp.readlines()]
width = len(grid[0])
height = len(grid)


class Coord:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __eq__(self, other):
        return (self.row, self.col) == (other.row, other.col)

    def __ne__(self, other):
        return (self.row, self.col) != (other.row, other.col)

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
start = Coord(0, grid[0].find("."))
end = Coord(len(grid) - 1, grid[-1].find("."))


def adjacent(coord: Coord, prev: Coord):
    adj = []
    back = prev - coord
    for d in (up, down, left, right):
        if d == back:
            continue
        n = coord + d
        if n == prev or n.row < 0 or n.row >= height or n.col < 0 or n.col >= width:
            continue
        sym = grid[n.row][n.col]
        if sym == "#":
            continue
        if (d, sym) in ((up, "v"), (down, "^"), (left, ">"), (right, "<")):
            continue
        else:
            adj.append(n)
    return adj


def walk(coord: Coord, prev: Coord):
    steps = 0
    nxt = adjacent(coord, prev)
    while len(nxt) == 1:
        prev = coord
        coord = nxt[0]
        steps += 1
        nxt = adjacent(coord, prev)

    if len(nxt) == 0:
        if coord == end:
            return steps
        else:
            return -1
    return steps + 1 + max(walk(n, coord) for n in nxt)


print(walk(start, Coord(-1, start.col)))
