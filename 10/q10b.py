def make_go_next(maze, width):

    def go_next(curr, prev):
        tile = maze[curr]
        if tile == "|" and prev < curr:
            return curr + width, 0
        if tile == "|" and prev > curr:
            return curr - width, 0
        if tile == "-" and prev < curr:
            return curr + 1, 0
        if tile == "-" and prev > curr:
            return curr - 1, 0
        if tile == "L" and prev < curr:
            return curr + 1, -1
        if tile == "L" and prev > curr:
            return curr - width, 1
        if tile == "J" and curr - prev == width:
            return curr - 1, 1
        if tile == "J" and curr - prev == 1:
            return curr - width, -1
        if tile == "7" and prev < curr:
            return curr + width, 1
        if tile == "7" and prev > curr:
            return curr - 1, -1
        if tile == "F" and prev - curr == 1:
            return curr + width, -1
        if tile == "F" and prev - curr == width:
            return curr + 1, 1
        print("WTF", curr, prev, maze[curr], maze[prev])

    return go_next


def make_left_right(maze, width, height):
    def boundary(curr):
        oob = set()
        if curr % width == 0:
            oob.update({curr - 1, curr - 1 - width, curr - 1 + width})
        if curr % width == width - 1:
            oob.update({curr + 1, curr + 1 - width, curr + 1 + width})
        if curr // width == 0:
            oob.update({curr - width, curr - width - 1, curr - width + 1})
        if curr // width == height - 1:
            oob.update({curr + width, curr + width - 1, curr + width + 1})
        return oob

    def left_right(curr, prev):
        tile = maze[curr]
        oob = boundary(curr)
        if tile == "|" and prev < curr:
            left = {curr + 1} - oob
            right = {curr - 1} - oob
        if tile == "|" and prev > curr:
            left = {curr - 1} - oob
            right = {curr + 1} - oob
        if tile == "-" and prev < curr:
            left = {curr - width} - oob
            right = {curr + width} - oob
        if tile == "-" and prev > curr:
            left = {curr + width} - oob
            right = {curr - width} - oob
        if tile == "L" and prev < curr:
            left = set()
            right = {curr - 1, curr + width - 1, curr + width} - oob
        if tile == "L" and prev > curr:
            left = {curr - 1, curr + width - 1, curr + width} - oob
            right = set()
        if tile == "J" and curr - prev == width:
            left = {curr + 1, curr + width, curr + width + 1} - oob
            right = set()
        if tile == "J" and curr - prev == 1:
            left = set()
            right = {curr + 1, curr + width, curr + width + 1} - oob
        if tile == "7" and prev < curr:
            left = {curr - width, curr - width + 1, curr + 1} - oob
            right = set()
        if tile == "7" and prev > curr:
            left = set()
            right = {curr - width, curr - width + 1, curr + 1} - oob
        if tile == "F" and prev - curr == 1:
            left = set()
            right = {curr - width, curr - width - 1, curr - 1} - oob
        if tile == "F" and prev - curr == width:
            left = {curr - width, curr - width - 1, curr - 1} - oob
            right = set()

        return left, right

    return left_right


def solve(init_curr, init_prev, go_next, left_right):
    curr = init_curr
    prev = init_prev

    left_set = set()  # set of coords on the left of the path
    right_set = set()  # set of coords on the right of the path
    path_set = set()  # set of coords on the path
    turns = 0  # number of right turns
    while True:
        path_set.add(curr)
        left, right = left_right(curr, prev)
        left_set.update(left)
        right_set.update(right)

        temp = curr
        curr, turn = go_next(curr, prev)
        turns += turn
        prev = temp

        if curr == init_curr:
            break

    if turns > 0:  # path was clockwise
        in_set = right_set
    else:
        in_set = left_set

    in_set -= path_set
    added_set = set()
    for coord in in_set:
        new = coord + 1
        while new not in in_set and new not in path_set:
            added_set.add(new)
            new += 1

    return in_set | added_set


if __name__ == "__main__":
    with open("input.txt") as fp:
        lines = fp.read().splitlines()
    width = len(lines[0])
    height = len(lines)
    maze = "".join(lines)
    start = maze.find("S")
    maze = maze.replace("S", "J")  # ok, I just looked at the file by eye
    next1 = start - 1
    enclosed = solve(next1, start, make_go_next(maze, width), make_left_right(maze, width, height))
    print(len(enclosed))
