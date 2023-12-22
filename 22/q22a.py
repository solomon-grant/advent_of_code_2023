import itertools
import queue


class Brick:
    def __init__(self, num, line: str):
        self.num = num
        pos, size = line.strip().split("~")
        self.x, self.y, self.z = tuple(int(n) for n in pos.strip("()").split(","))
        x_size, y_size, z_size = tuple(int(n) for n in size.strip("()").split(","))
        self.x_size = x_size - self.x + 1
        self.y_size = y_size - self.y + 1
        self.z_size = z_size - self.z + 1

        self.supports = set()
        self.supported_by = set()

    def __repr__(self):
        return f"{self.num}"

    def __hash__(self):
        return self.num

    def __eq__(self, other):
        return self.num == other.num

    def extent(self):
        """return an iterator over the x-y extent of this Brick"""
        return ((x, y) for x in range(self.x, self.x + self.x_size) for y in range(self.y, self.y + self.y_size))

    def removable(self):
        return all(len(b.supported_by) > 1 for b in self.supports)


with open("input.txt") as fp:
    bricks = [Brick(i, line) for i, line in enumerate(fp.readlines())]

bricks = sorted(bricks, key=lambda b: b.z)

max_x = max(b.x for b in bricks)
max_y = max(b.y for b in bricks)
grid = [[0] * (max_y + 1) for _ in range(max_x + 1)]
for b in bricks:
    z = max(grid[x][y] for x, y in b.extent())
    b.z = z + 1
    for x, y in b.extent():
        grid[x][y] = z + b.z_size
max_z = max(itertools.chain(*grid))

bricks = sorted(bricks, key=lambda b: b.z)
# for z in range(1, max_z + 1):
#     level = [["  .  "] * (max_y + 1) for _ in range(max_x + 1)]
#     for b in bricks:
#         if b.z <= z < b.z + b.z_size:
#             for x, y in b.extent():
#                 level[x][y] = str(b) + " " * (5 - len(str(b)))
#     print("Level", z)
#     for row in level:
#         print("".join(row))
#     print()

for i, b in enumerate(bricks):
    for other in bricks[i+1:]:
        if b.z + b.z_size == other.z and (set(b.extent()) & set(other.extent())):
            b.supports.add(other)
            other.supported_by.add(b)

removable = {b for b in bricks if b.removable()}
print(len(removable))  # part 1

total = 0
for brick in bricks:
    if brick in removable:
        continue
    falling = {b for b in brick.supports if len(b.supported_by) == 1}
    for b in bricks:
        if b.supported_by and b.supported_by <= falling:
            falling.add(b)
    total += len(falling)

print(total)  # part 2
