def ed(str1, str2):
    return sum(x != y for x, y in zip(str1, str2))


def find_reflection(rows):
    for i in range(1, len(rows)):
        if sum(ed(x, y) for x, y in zip(reversed(rows[:i]), rows[i:])) == 1:
            return 100 * i
    cols = list(zip(*rows))
    for i in range(1, len(cols)):
        if sum(ed(x, y) for x, y in zip(reversed(cols[:i]), cols[i:])) == 1:
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