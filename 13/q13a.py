def find_reflection(rows):
    for i in range(1, len(rows)):
        if all(x == y for x, y in zip(reversed(rows[:i]), rows[i:])) == 1:
            return 100 * i
    cols = list(zip(*rows))
    for i in range(1, len(cols)):
        if all(x == y for x, y in zip(reversed(cols[:i]), cols[i:])) == 1:
            return i


def solve(fname):
    with open(fname) as fp:
        contents = fp.read()

    total = 0
    for block in contents.split("\n\n"):
        total += find_reflection([row.strip() for row in block.split()])

    print(total)


if __name__ == "__main__":
    solve("example.txt")
    solve("input.txt")
