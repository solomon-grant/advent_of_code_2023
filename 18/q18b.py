import itertools


def decode(colour):
    # colour looks like (#XXXXXX)
    n = int(colour[2:7], 16)
    m = {
        0: "R",
        1: "D",
        2: "L",
        3: "U",
    }
    d = m[int(colour[7], 16)]
    return d, n


with open("example.txt") as fp:
    lines = fp.readlines()


min_height =
total = 0
for i, line in enumerate(lines):
    x, y = curr
    d, n = decode(line.strip().split()[2])

    if d == "L":
        x -= n
    if d == "R":
        horizontals.add(y)
        x += n
    if d == "U":
        v_segments.append((x, y, y+n))
        y += n
    if d == "D":
        v_segments.append((x, y-n, y))
        y -= n
    curr = (x, y)

for bot, top in itertools.pairwise(horizontals):
    verticals = [v for v in v_segments if v[1] <= bot < v[2]]
    for v1, v2 in itertools.pairwise(verticals):
        left = v1[0]
        right = v2[0]
        total += (top - bot) * (right - left)
        print("bot:", bot, "top:", top, "left:", left, "right:", right)

print(total)
