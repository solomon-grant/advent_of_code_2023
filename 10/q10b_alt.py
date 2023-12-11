class Tile:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __add__(self, other):
        return Tile(self.row + other.row, self.col + other.col)

    def __sub__(self, other):
        return Tile(self.row - other.row, self.col - other.col)

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __ne__(self, other):
        return self.row != other.row or self.col != other.col

    def __hash__(self):
        return self.row * 1000 + self.col


UP = Tile(-1, 0)
DOWN = Tile(1, 0)
LEFT = Tile(0, -1)
RIGHT = Tile(0, 1)


def going(_from, _to):
    return _to - _from


def make_go_next(maze):

    def go_next(curr, prev):
        tile = maze[curr.row][curr.col]
        heading = going(prev, curr)
        if tile == "|" and heading == DOWN:
            return curr + DOWN, 0
        if tile == "|" and heading == UP:
            return curr + UP, 0
        if tile == "-" and heading == RIGHT:
            return curr + RIGHT, 0
        if tile == "-" and heading == LEFT:
            return curr + LEFT, 0
        if tile == "L" and heading == DOWN:
            return curr + RIGHT, -1
        if tile == "L" and heading == LEFT:
            return curr + UP, 1
        if tile == "J" and heading == DOWN:
            return curr + LEFT, 1
        if tile == "J" and heading == RIGHT:
            return curr + UP, -1
        if tile == "7" and heading == RIGHT:
            return curr + DOWN, 1
        if tile == "7" and heading == UP:
            return curr + LEFT, -1
        if tile == "F" and heading == UP:
            return curr + RIGHT, 1
        if tile == "F" and heading == LEFT:
            return curr + DOWN, -1

    return go_next


def make_boundary(maze):
    width = len(maze[0])
    height = len(maze)
    
    def boundary(tiles):
        return {tile for tile in tiles if 0 <= tile.row < height and 0 <= tile.col < width}
    
    return boundary


def make_left_right(maze):
    
    def left_right(curr, prev):
        tile = maze[curr.row][curr.col]
        heading = going(prev, curr)
        if tile == "|" and heading == UP:
            left = {curr + LEFT}
            right = {curr + RIGHT}
        if tile == "|" and heading == DOWN:
            left = {curr + RIGHT}
            right = {curr + LEFT}
        if tile == "-" and heading == RIGHT:
            left = {curr + UP}
            right = {curr + DOWN}
        if tile == "-" and heading == LEFT:
            left = {curr + DOWN}
            right = {curr + UP}
        if tile == "L" and heading == DOWN:
            left = set()
            right = {curr + LEFT, curr + DOWN, curr + LEFT + DOWN}
        if tile == "L" and heading == LEFT:
            left = {curr + DOWN, curr + LEFT, curr + DOWN + LEFT}
            right = set()
        if tile == "J" and heading == DOWN:
            left = {curr + RIGHT, curr + DOWN, curr + RIGHT + DOWN}
            right = set()
        if tile == "J" and heading == RIGHT:
            left = set()
            right = {curr + DOWN, curr + RIGHT, curr + RIGHT + DOWN}
        if tile == "7" and heading == RIGHT:
            left = {curr + UP, curr + RIGHT, curr + UP + RIGHT}
            right = set()
        if tile == "7" and heading == UP:
            left = set()
            right = {curr + RIGHT, curr + UP, curr + UP + RIGHT}
        if tile == "F" and heading == LEFT:
            left = set()
            right = {curr + UP, curr + LEFT, curr + UP + LEFT}
        if tile == "F" and heading == UP:
            left = {curr + LEFT, curr + UP, curr + LEFT + UP}
            right = set()

        return left, right

    return left_right


def solve(init_curr, init_prev, go_next, left_right, boundary):
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
    in_set = boundary(in_set)
    added_set = set()
    for tile in in_set:
        new = tile + RIGHT
        while new not in in_set and new not in path_set:
            added_set.add(new)
            new += RIGHT

    return in_set | added_set


if __name__ == "__main__":
    with open("input.txt") as fp:
        maze = fp.read().splitlines()

    for row, chars in enumerate(maze):
        for col, char in enumerate(chars):
            if char == "S":
                start = Tile(row, col)

    maze[start.row] = maze[start.row][:start.col] + "J" + maze[start.row][start.col + 1:]
    next1 = start + LEFT
    enclosed = solve(next1, start, make_go_next(maze), make_left_right(maze), make_boundary(maze))
    print(len(enclosed))
