with open("input.txt") as fp:
    file = fp.read()

chunks = file.split("\n\n")
seeds = list(map(int, chunks[0].split(":")[1].strip().split()))
maps = [chunk.split(":")[1].strip().split("\n") for chunk in chunks[1:]]

locations = []
for seed in seeds:
    curr = seed
    for m in maps:
        for line in m:
            dest, source, length = list(map(int, line.split()))
            diff = curr - source
            if diff > length or diff < 0:
                continue
            curr = dest + diff
            break
    locations.append(curr)
print(min(locations))

