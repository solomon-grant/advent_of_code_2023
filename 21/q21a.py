# insight: any closed loop on a grid has even length
# => any grid square which can be reached from S in an even number of steps is reachable in exactly 64 steps
# => any grid square which can only be reached in an odd number of steps is not reachable in exactly 64 steps
import collections
import queue

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
print(s)
N, E, S, W = (-1, 0), (0, 1), (1, 0), (0, -1)

seen = dict()
q = collections.deque([(0, s)])
while q:
    d, u = q.popleft()
    if u in seen:
        continue
    seen[u] = d
    for step in (N, E, S, W):
        row, col = u[0] + step[0], u[1] + step[1]
        if row < 0 or row >= height or col < 0 or col >= height or grid[row][col] == "#":
            continue
        q.append((d + 1, (row, col)))

reachable = len([n for n, d in seen.items() if d <= 64 and (d % 2) == 0])
print(reachable)


