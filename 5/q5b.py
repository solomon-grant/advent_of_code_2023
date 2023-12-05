import re


with open("input.txt") as fp:
    file = fp.read()


def intersect(r1, r2):
    s1, e1 = r1
    s2, e2 = r2
    if e1 <= s2 or s1 >= e2:
        return [], [r1]
    if s2 <= s1 and e1 <= e2:
        return [r1], []
    if s1 <= s2 and e1 >= e2:
        if s1 == s2:
            return [r2], [(e2, e1)]
        if e1 == e2:
            return [r2], [(s1, s2)]
        return [r2], [(s1, s2), (e2, e1)]
    if s1 < s2 < e1 < e2:
        return [(s2, e1)], [(s1, s2)]
    if s2 < s1 < e2 < e1:
        return [(s1, e2)], [(e2, e1)]
    raise ValueError(f"Bad intersection: {r1}, {r2}")


def do_map_line(ranges, map_line):
    dest, src, length = list(map(int, map_line.split()))
    offset = dest - src

    mapped = []
    unmapped = []
    for r in ranges:
        intersection_ranges, other_ranges = intersect(r, (src, src + length))
        mapped.extend([(start + offset, end + offset) for start, end in intersection_ranges])
        unmapped.extend(other_ranges)

    return mapped, unmapped


def do_map(ranges, m):
    mapped = []
    to_do = list(ranges)
    for line in m:
        _mapped, unmapped = do_map_line(to_do, line)
        mapped.extend(_mapped)
        to_do = unmapped
    mapped.extend(to_do)
    return mapped


if __name__ == "__main__":
    with open("input.txt") as fp:
        file = fp.read()

    chunks = file.split("\n\n")
    seed_ranges = [(int(m.group(1)), int(m.group(2))) for m in re.finditer(r"(\d+) (\d+)", chunks[0].split(":")[1].strip())]
    maps = [chunk.split(":")[1].strip().split("\n") for chunk in chunks[1:]]

    ranges = [(s, s+n) for s, n in seed_ranges]
    for m in maps:
        ranges = do_map(ranges, m)

    print(min(x[0] for x in ranges))
