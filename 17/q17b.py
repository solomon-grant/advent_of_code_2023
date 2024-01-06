import queue

steps = {
    "U": (-1, 0),
    "R": (0, 1),
    "D": (1, 0),
    "L": (0, -1),
}

back = {
    "U": "D",
    "D": "U",
    "L": "R",
    "R": "L",
}

with open("input.txt") as fp:
    grid = [[int(x) for x in line.strip()] for line in fp.readlines()]

height = len(grid)
width = len(grid[0])
fin = (height - 1, width - 1)

min_steps = 4
max_steps = 10


def dijkstra(d_init, row_init, col_init, path_init):
    s = dict()
    q = queue.PriorityQueue()
    q.put((d_init, (row_init, col_init, path_init)))
    while not q.empty():
        d, (row, col, path) = q.get()
        last_step = path[-1] if path else ""
        enter = last_step * (len(path) - len(path.rstrip(last_step)))
        if (row, col, enter) in s:
            continue
        s[(row, col, enter)] = d
        if (row, col) == fin:
            continue
        if len(enter) < min_steps:
            r, c = steps[last_step]
            new_row = row + r
            new_col = col + c
            if new_row < 0 or new_row >= height or new_col < 0 or new_col >= width:
                continue
            q.put((d + grid[new_row][new_col], (new_row, new_col, path + last_step)))
        else:
            for step, (r, c) in steps.items():
                if path and step == back[last_step]:
                    continue
                if path[-max_steps:] == max_steps * step:
                    continue
                new_row = row + r
                new_col = col + c
                if new_row < 0 or new_row >= height or new_col < 0 or new_col >= width:
                    continue
                q.put((d + grid[new_row][new_col], (new_row, new_col, path + step)))
    return min(d for (r, c, _), d in s.items() if (r, c) == fin)


print(min(dijkstra(grid[0][1], 0, 1, "R"), dijkstra(grid[1][0], 1, 0, "D")))



