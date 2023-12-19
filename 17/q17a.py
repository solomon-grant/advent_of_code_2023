import itertools
from queue import PriorityQueue


def solve(fname):
    with open(fname) as fp:
        grid = [[int(x) for x in line.strip()] for line in fp.readlines()]
    height = len(grid)
    width = len(grid[0])
    inf = sum(itertools.chain(*grid)) + 1

    # cache[i][j] stores the weight and path of an optimal path from (0,0) to (i,j)
    cache = [[(inf, "")] * width for _ in range(height)]
    cache[0][0] = (0, "")

    # dijkstra's algorithm for single-source shortest paths
    q = PriorityQueue()
    q.put((0, (0, 0)))
    while not q.empty():
        z, (row, col) = q.get()
        val, path = cache[row][col]
        for (next_row, next_col), next_direction in (((row - 1, col), "U"), ((row + 1, col), "D"), ((row, col - 1), "L"), ((row, col + 1), "R")):
            if next_row < 0 or next_row >= height or next_col < 0 or next_col >= width:
                continue
            next_path = path + next_direction
            if next_path[-2:] in ("UD", "DU", "LR", "RL") or next_path[-4:] in ("UUUU", "DDDD", "LLLL", "RRRR"):
                continue
            next_val = val + grid[next_row][next_col]
            if cache[next_row][next_col][0] > next_val:
                cache[next_row][next_col] = (next_val, next_path)
                q.put((next_val, (next_row, next_col)))

    # # bellman-ford algorithm
    # for _ in range(width * height - 1):
    #     for row in range(height):
    #         for col in range(height):
    #             val, path = cache[row][col]
    #             for (next_row, next_col), next_direction in (((row - 1, col), "U"), ((row + 1, col), "D"), ((row, col - 1), "L"), ((row, col + 1), "R")):
    #                 if next_row < 0 or next_row >= height or next_col < 0 or next_col >= width:
    #                     continue
    #                 next_path = path + next_direction
    #                 if next_path[-2:] in ("UD", "DU", "LR", "RL") or next_path[-4:] in ("UUUU", "DDDD", "LLLL", "RRRR"):
    #                     continue
    #                 next_val = val + grid[next_row][next_col]
    #                 if cache[next_row][next_col][0] > next_val:
    #                     cache[next_row][next_col] = (next_val, next_path)

    for row in cache:
        print(" ".join([str(x[0]) for x in row]))


if __name__ == "__main__":
    solve("example.txt")

