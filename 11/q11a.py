class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(a, b):
    return abs(b.x - a.x) + abs(b.y - a.y)


def solve(sky):
    galaxies = []
    empty_rows = set()
    non_empty_cols = set()
    for y, row in enumerate(sky):
        found = False
        for x, point in enumerate(row):
            if point == "#":
                found = True
                non_empty_cols.add(x)
                galaxies.append(Point(x, y))
        if not found:
            empty_rows.add(y)
    empty_cols = [c for c in range(len(sky[0])) if c not in non_empty_cols]

    def expand(a, b):
        rows = [r for r in empty_rows if min(a.y, b.y) < r < max(a.y, b.y)]
        cols = [c for c in empty_cols if min(a.x, b.x) < c < max(a.x, b.x)]
        return 999_999 * (len(rows) + len(cols))

    sum = 0
    for i, a in enumerate(galaxies[:-1]):
        for b in galaxies[i+1:]:
            sum += distance(b, a) + expand(a, b)

    return sum


if __name__ == "__main__":
    with open("input.txt") as fp:
        sky = fp.readlines()
    sky = [row.strip() for row in sky]
    print(solve(sky))
