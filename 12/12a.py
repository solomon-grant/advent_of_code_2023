import itertools
import re


def get_contigs(row: str, choice: tuple):
    row = list(row)
    for i in choice:
        row[i] = "#"
    row = "".join(row)
    return [len(g) for g in re.findall(r"#+", row)]


def brute_force(row: str, unknowns: list, contigs: list):
    row = row.replace("?", ".")
    r = sum(contigs) - row.count("#")
    ways = 0
    for choice in itertools.combinations(unknowns, r):
        if get_contigs(row, choice) == contigs:
            ways += 1
    return ways


def solve(row: str):
    row, contigs = row.strip().split()
    unknowns = [i for i, x in enumerate(row) if x == "?"]
    contigs = [int(x) for x in contigs.split(",")]
    return brute_force(row, unknowns, contigs)


if __name__ == "__main__":
    with open("input.txt") as fp:
        print(sum(solve(line) for line in fp.readlines()))
