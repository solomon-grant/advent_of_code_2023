# insight: any closed loop on a grid has even length
# => any grid square which can be reached from S in an even number of steps is reachable in exactly 64 steps
# => any grid square which can only be reached in an odd number of steps is not reachable in exactly 64 steps
import collections
import itertools

# if P(S,d) is the set of all paths of length <= 64 from S to d, want to find all x such that len(p) is odd for all p
# in P(S,d).
# lemma: if the length of the shortest path from S to d is odd, then all paths from S to d are odd.
# -- shortest possible path length is d_x - S_x + d_y - S_y

# idea: use Dijkstra's alg to find SSSP to each grid square. Then eliminate the ones where the path is odd.
with open("input.txt") as fp:
    grid = [line.strip() for line in fp.readlines()]

width = len(grid[0])
height = len(grid)
s = next((i, j) for i in range(height) for j in range(width) if grid[i][j] == "S")
N, E, S, W = (-1, 0), (0, 1), (1, 0), (0, -1)


def dijkstra(start):
    seen = [[-1] * width for _ in range(height)]
    q = collections.deque([(0, start)])
    while q:
        d, (r, c) = q.popleft()
        if seen[r][c] >= 0:
            continue
        seen[r][c] = d
        for step in (N, E, S, W):
            row, col = r + step[0], c + step[1]
            if row < 0 or row >= height or col < 0 or col >= height or grid[row][col] == "#":
                continue
            q.append((d + 1, (row, col)))
    return seen


def reachable(d, steps):
    return sum(((0 <= x <= steps) and (x % 2 == steps % 2)) for x in itertools.chain(*d))


NORTH = (0, s[1])
NORTHEAST = (0, width - 1)
EAST = (s[0], width - 1)
SOUTHEAST = (height - 1, width - 1)
SOUTH = (height - 1, s[1])
SOUTHWEST = (height - 1, 0)
WEST = (s[0], 0)
NORTHWEST = (0, 0)

distances = [dijkstra(c) for c in [NORTH, EAST, SOUTH, WEST]]
d_max = [max(itertools.chain(*d)) for d in distances]
w_even = [reachable(d, m + (m % 2)) for d, m in zip(distances, d_max)]
w_odd = [reachable(d, m + 1 + (m % 2)) for d, m in zip(distances, d_max)]

diagonals = [dijkstra(c) for c in [NORTHEAST, SOUTHEAST, SOUTHWEST, NORTHWEST]]
di_max = [max(itertools.chain(*d)) for d in diagonals]
wi_even = [reachable(d, m + (m % 2)) for d, m in zip(diagonals, di_max)]
wi_odd = [reachable(d, m + 1 + (m % 2)) for d, m in zip(diagonals, di_max)]

steps = 26501365
total = reachable(dijkstra(s), steps)
steps -= (65 + 1)

while steps > 0:
    if steps % 2 == 0:
        weights = w_even
    else:
        weights = w_odd
    for d, m, w in zip(distances, d_max, weights):
        total += w if steps >= m else reachable(d, steps)

    steps -= 131


steps = 26501365
steps -= 2 * (65 + 1)
shell = 1
while steps > 0:
    if steps % 2 == 0:
        weights = wi_even
    else:
        weights = wi_odd
    for d, m, w in zip(diagonals, di_max, weights):
        total += shell * (w if steps >= m else reachable(d, steps))
    steps -= 131
    shell += 1

print(total)
