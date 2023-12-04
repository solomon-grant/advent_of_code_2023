from collections import defaultdict
with open("input.txt") as fp:
    copies = defaultdict(int)
    total = 0
    for line in fp:
        card_num, nums = line.split(":")
        card_num = int(card_num.split()[1])
        copies[card_num] += 1
        total += copies[card_num]

        need, have = nums.split("|")
        need = need.strip().split()
        have = have.strip().split()
        matches = len([x for x in have if x in need])
        for skip in range(1, matches + 1):
            copies[card_num + skip] += copies[card_num]
    print(total)
