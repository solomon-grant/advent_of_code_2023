with open("input.txt") as fp:
    total = 0
    for line in fp:
        need, have = line.split(":")[1].split("|")
        need = need.strip().split()
        have = have.strip().split()
        points = 0
        for num in have:
            if num in need:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        total += points
    print(total)
