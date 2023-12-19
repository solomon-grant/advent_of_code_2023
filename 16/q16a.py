def propagate(initial, grid):
    beams = [initial]
    energized = set()
    beam_cache = set()

    height = len(grid)
    width = len(grid[0])

    while beams:
        beam = beams.pop()
        if beam in beam_cache:
            continue
        beam_cache.add(beam)

        tile, direction = beam
        row, col = tile
        if row < 0 or row == height or col < 0 or col == width:
            continue
        energized.add(tile)

        sym = grid[row][col]
        if sym == ".":
            if direction == "U":
                row -= 1
            if direction == "D":
                row += 1
            if direction == "R":
                col += 1
            if direction == "L":
                col -= 1
            beams.append(((row, col), direction))
        if sym == "/":
            if direction == "U":
                beams.append(((row, col+1), "R"))
            if direction == "D":
                beams.append(((row, col-1), "L"))
            if direction == "R":
                beams.append(((row-1, col), "U"))
            if direction == "L":
                beams.append(((row+1, col), "D"))
        if sym == "\\":
            if direction == "U":
                beams.append(((row, col-1), "L"))
            if direction == "D":
                beams.append(((row, col+1), "R"))
            if direction == "R":
                beams.append(((row+1, col), "D"))
            if direction == "L":
                beams.append(((row-1, col), "U"))
        if sym == "-":
            if direction == "U" or direction == "D":
                beams.append(((row, col+1), "R"))
                beams.append(((row, col-1), "L"))
            if direction == "R":
                beams.append(((row, col+1), direction))
            if direction == "L":
                beams.append(((row, col-1), direction))
        if sym == "|":
            if direction == "U":
                beams.append(((row-1, col), direction))
            if direction == "D":
                beams.append(((row+1, col), direction))
            if direction == "R" or direction == "L":
                beams.append(((row+1, col), "D"))
                beams.append(((row-1, col), "U"))

    return len(energized)


def solve(fname):
    with open(fname) as fp:
        grid = [line.strip() for line in fp.readlines()]

    height = len(grid)
    width = len(grid[0])

    max_energized = 0
    for row in range(height):
        energized = propagate(((row, 0), "R"), grid)
        if energized > max_energized:
            max_energized = energized
        energized = propagate(((row, width-1), "L"), grid)
        if energized > max_energized:
            max_energized = energized
    for col in range(width):
        energized = propagate(((0, col), "D"), grid)
        if energized > max_energized:
            max_energized = energized
        energized = propagate(((height-1, col), "U"), grid)
        if energized > max_energized:
            max_energized = energized

    print(max_energized)


solve("example.txt")
solve("input.txt")
