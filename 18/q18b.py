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


right_turns = ("UR", "RD", "DL", "LU")

with open("input.txt") as fp:
    lines = fp.readlines()


min_height = 0
max_height = 0
height = 0
prev_d, _ = decode(lines[-1].strip().split()[2])
horizontals = []
for i, line in enumerate(lines):
    d, n = decode(line.strip().split()[2])
    next_d, _ = decode(lines[(i+1) % len(lines)].strip().split()[2])
    turn_in = prev_d + d
    turn_out = d + next_d
    # d, n, _ = line.strip().split()
    n = int(n)
    if turn_in in right_turns and turn_out in right_turns:
        n += 1
    if turn_in not in right_turns and turn_out not in right_turns:
        n -= 1
    if d == "L":
        horizontals.append((-n, height))
    if d == "R":
        horizontals.append((n, height))
    if d == "U":
        height += n
    if d == "D":
        height -= n
        min_height = min(min_height, height)
    prev_d = d

total = sum(w * (h - min_height) for w, h in horizontals)
print(total)
