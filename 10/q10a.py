def make_go_next(maze, width):

    def go_next(curr, prev):
        tile = maze[curr]
        if tile == "|" and prev < curr:
            return curr + width
        if tile == "|" and prev > curr:
            return curr - width
        if tile == "-" and prev < curr:
            return curr + 1
        if tile == "-" and prev > curr:
            return curr - 1
        if tile == "L" and prev < curr:
            return curr + 1
        if tile == "L" and prev > curr:
            return curr - width
        if tile == "J" and curr - prev == width:
            return curr - 1
        if tile == "J" and curr - prev == 1:
            return curr - width
        if tile == "7" and prev < curr:
            return curr + width
        if tile == "7" and prev > curr:
            return curr - 1
        if tile == "F" and prev - curr == 1:
            return curr + width
        if tile == "F" and prev - curr == width:
            return curr + 1

    return go_next


def solve(start, next1, next2, go_next):
    curr1 = next1
    prev1 = start
    curr2 = next2
    prev2 = start

    count = 1  # we already took one step from the start
    while curr1 != curr2:
        temp = curr1
        curr1 = go_next(curr1, prev1)
        prev1 = temp
        temp = curr2
        curr2 = go_next(curr2, prev2)
        prev2 = temp
        count += 1

    return count


if __name__ == "__main__":
    with open("input.txt") as fp:
        lines = fp.read().splitlines()
    width = len(lines[0])
    maze = "".join(lines)
    start = maze.find("S")
    next1 = start - 1
    next2 = start - width
    print(solve(start, next1, next2, make_go_next(maze, width)))
