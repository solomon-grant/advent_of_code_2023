from collections import defaultdict


# places in chunk where you could put the given contig as the first contig
def place_first(chunk: str, contig: int) -> list:
    if contig > len(chunk):
        return []
    first_known = chunk.find("#")
    could_go_here = []
    for start in range(len(chunk) - contig + 1):
        end = start + contig
        if first_known >= 0 and start == first_known + 1:  # the contig will no longer be the first contig in this chunk since
            break
        if end < len(chunk) and chunk[end] == "#":
            continue
        if any(chunk[i] == "." for i in range(start, end)):  # can't put the contig in this subchunk
            continue
        could_go_here.append(start)
    return could_go_here


# count the number of ways to allocate these contigs into this chunk
def ways(chunk, contigs, memo):
    i = len(chunk)
    j = len(contigs)
    if memo[i][j] >= 0:
        return memo[i][j]

    if i == 0:
        if j > 0:
            memo[i][j] = 0
            return 0
        memo[i][j] = 1
        return 1
    elif j == 0:
        if "#" in chunk:
            memo[i][j] = 0
            return 0
        memo[i][j] = 1
        return 1

    contig = contigs[0]
    rest = contigs[1:]
    count = 0
    for place in place_first(chunk, contig):
        next_chunk = chunk[place + contig + 1:]
        count += ways(next_chunk, rest, memo)
    memo[i][j] = count
    return count


def unfold(row, contigs):
    row = "?".join([row] * 5)
    contigs = ",".join([contigs] * 5)
    return row, contigs


def solve(row: str):
    row, contigs = row.strip().split()
    row, contigs = unfold(row, contigs)
    contigs = [int(x) for x in contigs.split(",")]
    memo = defaultdict(lambda: defaultdict(lambda: -1))
    return ways(row, contigs, memo)


if __name__ == "__main__":
    with open("input.txt") as fp:
        print(sum(solve(line) for line in fp.readlines()))
