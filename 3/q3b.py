import re

num_map = dict()
num_sets = dict()
num_re = re.compile(r"\d+")
with open("input.txt") as fp:
    for i, line in enumerate(fp):
        for match in num_re.finditer(line):
            num = int(match.group(0))
            num_set = set()
            for j in range(*match.span()):
                num_map[(i, j)] = num
                num_set.add((i, j))
            for j in range(*match.span()):
                num_sets[(i, j)] = num_set


def around(line_index, start, end):
    left = start - 1
    right = end + 1
    top_coords = [(line_index - 1, z) for z in range(left, right)]
    side_coords = [(line_index, left), (line_index, end)]
    bottom_coords = [(line_index + 1, z) for z in range(left, right)]
    return top_coords + side_coords + bottom_coords


total = 0
with open("input.txt") as fp:
    for i, line in enumerate(fp):
        for j, char in enumerate(line):
            if char == "*":
                seen = set()
                nums = []
                for coord in around(i, j, j+1):
                    if coord in num_map and coord not in seen:
                        nums.append(num_map[coord])
                        seen = seen.union(num_sets[coord])
                if len(nums) == 2:
                    total += nums[0] * nums[1]

print(total)
