with open("input.txt") as fp:
    stones = []
    for line in fp.readlines():
        pos, vel = line.strip().split(" @ ")
        stones.append((tuple(int(p) for p in pos.split(", ")[:2]), tuple(int(v) for v in vel.split(", ")[:2])))

min_ = 200000000000000
max_ = 400000000000000


def intersect2d(px1, py1, vx1, vy1, px2, py2, vx2, vy2):
    # intersection of p1 + v1t and p2 + v2s
    # =>   px1 + vx1 * t == px2 + vx2 * s
    # and  py1 + vy1 * t == py2 + vy2 * s

    # =>   vx1 * t == px2 - px1 + vx2 * s
    # =>   vy1 * (px2 - px1 + vx2 * s) == vx1 * (py2 - py1 + vy2 * s)
    # =>   vy1 * px2 - vy1 * px1 + vy1 * vx2 * s == vx1 * py2 - vx1 * py1 + vx1 * vy2 * s

    # =>   s * (vy1 * vx2 - vx1 * vy2) == vx1 * (py2 - py1) - vy1 * (px2 - px1)
    # =>   (vy1 * vx2 - vx1 * vy2) * (vx1 * t + px1 - px2) == vx2 * (vx1 * (py2 - py1) - vy1 * (px2 - px1))
    # =>   (vy1)(vx2)(vx1)t + (vy1)(vx2)(px1) - (vy1)(vx2)(px2) - (vx1)(vy2)(vx1)(t) - (vx1)(vy2)(px1) + (vx1)(vy2)(px2) == (vx2)(vx1)(py2) - (vx2)(vx1)(py1) - (vx2)(vy1)(px2) + (vx2)(vy1)(px1)
    # =>   ((vy1)(vx2) - (vy2)(vx1))t == (vx2)(py2) - (vx2)(py1) + (vy2)(px1) - (vy2)(px2)
    s_num = vx1 * (py2 - py1) - vy1 * (px2 - px1)
    t_num = vx2 * (py2 - py1) + vy2 * (px1 - px2)
    denom = vy1 * vx2 - vx1 * vy2

    if denom == 0:
        return None  # lines are parallel
    if (denom < 0 and (s_num > 0 or t_num > 0)) or (denom > 0 and (s_num < 0 or t_num < 0)):
        return None  # s or t is negative

    t = t_num / denom
    x = px1 + vx1 * t
    y = py1 + vy1 * t
    if x < min_ or x > max_ or y < min_ or y > max_:
        return None
    print(x,y)
    return x, y


intersections = 0
for i, (p1, v1) in enumerate(stones):
    for (p2, v2) in stones[i+1:]:
        if intersect2d(*p1, *v1, *p2, *v2) is not None:
            intersections += 1

print(intersections)
