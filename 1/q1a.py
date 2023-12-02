import re

with open("input.txt") as fp:
    pattern = re.compile("\d")
    print(sum(int(pattern.search(line)[0] + pattern.search(line[::-1])[0]) for line in fp))
