from collections import defaultdict

with open("input.txt") as fp:
    codes = fp.read()


def HASH(s):
    val = 0
    for c in s:
        val += + ord(c)
        val *= 17
        val %= 256
    return val


hashmap = defaultdict(dict)
for code in codes.split(","):
    if "=" in code:
        prefix, num = code.split("=")
        hashmap[HASH(prefix)][prefix] = num
    elif "-" in code:
        prefix, num = code.split("-")
        if prefix in hashmap[HASH(prefix)]:
            hashmap[HASH(prefix)].pop(prefix)

total = 0
for i in range(256):
    for j, v in enumerate(hashmap[i].values()):
        total += (i + 1) * (j + 1) * int(v)

print(total)

