import re

syms = {'#', '+', '/', '*', '=', '-', '&', '%', '@', '$'}
sym_coords = set()
with open("input.txt") as fp:
    for i, line in enumerate(fp):
        for j, char in enumerate(line):
            if char in syms:
                sym_coords.add((i, j))


def around(line_index, start, end):
    left = start - 1
    right = end + 1
    top_coords = [(line_index - 1, z) for z in range(left, right)]
    side_coords = [(line_index, left), (line_index, end)]
    bottom_coords = [(line_index + 1, z) for z in range(left, right)]
    return top_coords + side_coords + bottom_coords


total = 0
numre = re.compile(r"\d+")
with open("input.txt") as fp:
    for i, line in enumerate(fp):
        for match in numre.finditer(line):
            for coord in around(i, match.start(), match.end()):
                if coord in sym_coords:
                    total += int(match.group(0))
                    break

print(total)
