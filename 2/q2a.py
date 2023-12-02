def get_counts(s):
    r = 0
    g = 0
    b = 0
    for part in s.split(","):
        num, colour = part.strip().split()
        if colour == "red":
            r += int(num)
        elif colour == "green":
            g += int(num)
        elif colour == "blue":
            b += int(num)
    return r, g, b


def is_possible(game, maxr, maxg, maxb):
    sets = game.split(";")
    for s in sets:
        r, g, b = get_counts(s)
        if r > maxr or g > maxg or b > maxb:
            return False
    return True


with open("input.txt") as fp:
    gamesum = 0
    for line in fp:
        game_id, game = line.split(": ")
        if is_possible(game, 12, 13, 14):
            gamesum += int(game_id.split()[-1])
    print(gamesum)
