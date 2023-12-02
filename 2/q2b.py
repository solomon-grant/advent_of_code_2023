def get_counts(s):
    r = 0
    g = 0
    b = 0
    for part in s.split(", "):
        num, colour = part.split()
        if colour == "red":
            r += int(num)
        elif colour == "green":
            g += int(num)
        elif colour == "blue":
            b += int(num)
    return r, g, b


def get_power(game):
    maxr = 0
    maxg = 0
    maxb = 0
    for draw in game.split("; "):
        r, g, b = get_counts(draw)
        maxr = max(maxr, r)
        maxg = max(maxg, g)
        maxb = max(maxb, b)
    return maxr * maxg * maxb


with open("input.txt") as fp:
    powersum = 0
    for line in fp:
        game = line.split(": ")[1]
        powersum += get_power(game)
    print(powersum)
