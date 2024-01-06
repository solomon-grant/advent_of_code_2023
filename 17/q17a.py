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
inf = sum(sum(line) for line in grid) + 1

visited = set()

def dijkstra():
    s = dict()
    q = queue.PriorityQueue()
    q.put((0, (0, 0, "")))
    while not q.empty():
        d, (row, col, path) = q.get()
        last_step = path[-1] if path else ""
        enter = last_step * (len(path) - len(path.rstrip(last_step)))
        if (row, col, enter) in s:
            continue
        s[(row, col, enter)] = d
        if (row, col) == fin:
            continue
        for step, (r, c) in steps.items():
            if path and step == back[last_step]:
                continue
            if path[-3:] == 3 * step:
                continue
            new_row = row + r
            new_col = col + c
            if new_row < 0 or new_row >= height or new_col < 0 or new_col >= width:
                continue
            q.put((d + grid[new_row][new_col], (new_row, new_col, path + step)))
    print(min(d for (r, c, _), d in s.items() if (r, c) == fin))

dijkstra()



