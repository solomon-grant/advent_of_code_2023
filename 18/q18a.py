with open("example.txt") as fp:
    lines = fp.readlines()

trench = set()
left_set = set()
right_set = set()
min_x = 0
max_x = 0
min_y = 0
max_y = 0
curr = (0, 0)
prev_direction = ""
right_turns = 0
for line in lines:
    d, n, c = line.strip().split()

    seq = prev_direction + d
    x, y = curr
    if seq in ("UR", "RD", "DL", "LU"):
        right_turns += 1
        if seq == "UR":
            left_set.add((x - 1, y + 1))
            left_set.add((x, y + 1))
        if seq == "RD":
            left_set.add((x + 1, y + 1))
            left_set.add((x + 1, y))
        if seq == "DL":
            left_set.add((x, y - 1))
            left_set.add((x + 1, y - 1))
        if seq == "LU":
            left_set.add((x - 1, y - 1))
            left_set.add((x - 1, y))
    elif seq in ("UL", "LD", "DR", "RU"):
        right_turns -= 1
        if seq == "UL":
            right_set.add((x + 1, y + 1))
            right_set.add((x, y + 1))
        if seq == "LD":
            right_set.add((x - 1, y + 1))
            right_set.add((x - 1, y))
        if seq == "DR":
            right_set.add((x - 1, y - 1))
            right_set.add((x, y - 1))
        if seq == "RU":
            right_set.add((x + 1, y - 1))
            right_set.add((x + 1, y))

    for _ in range(int(n)):
        x, y = curr
        if d == "U":
            y += 1
        if d == "D":
            y -= 1
        if d == "L":
            x -= 1
        if d == "R":
            x += 1

        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y

        curr = (x, y)
        trench.add(curr)
        if d == "U":
            left_set.add((x - 1, y))
            right_set.add((x + 1, y))
        if d == "D":
            left_set.add((x + 1, y))
            right_set.add((x - 1, y))
        if d == "L":
            left_set.add((x, y - 1))
            right_set.add((x, y + 1))
        if d == "R":
            left_set.add((x, y + 1))
            right_set.add((x, y - 1))

    prev_direction = d

if right_turns > 0:
    bdy = right_set
else:
    bdy = left_set
bdy -= trench

fill = set()
for coord in bdy:
    x, y = coord
    x += 1
    while (x, y) not in fill and (x, y) not in trench:
        fill.add((x, y))
        x += 1

fill = fill.union(bdy)

for row in range(max_y, min_y - 1, -1):
    print("".join(["#" if (col, row) in trench else "X" if (col, row) in fill else "." for col in range(min_x, max_x + 1)]))

print(len(trench) + len(fill))
