from collections import defaultdict, deque


def make_graph(fname):
    t = defaultdict(str)
    in_ = defaultdict(list)
    out = defaultdict(list)
    with open(fname) as fp:
        for line in fp.readlines():
            name, to = line.strip().split(" -> ")
            if name[0] in "%&":
                type_, name = name[0], name[1:]
                t[name] = type_
            out[name] = to.split(", ")
            for n in out[name]:
                in_[n].append(name)
    return t, in_, out


LO = 0
HI = 1

t, in_, out = make_graph("input.txt")
state = {n: LO for n in t}
state["broadcaster"] = LO


def push():
    hi_pulses = 0
    lo_pulses = 1  # button
    q = deque([("broadcaster", n, LO) for n in out["broadcaster"]])
    while q:
        src, dest, pulse = q.popleft()
        if pulse == HI:
            hi_pulses += 1
        else:
            lo_pulses += 1
        type_ = t[dest]
        if type_ == "%" and pulse == LO:
            state[dest] = LO if state[dest] == HI else HI
            q.extend([(dest, n, state[dest]) for n in out[dest]])
        if type_ == "&":
            if all([state[n] == HI for n in in_[dest]]):
                state[dest] = LO
            else:
                state[dest] = HI
            q.extend([(dest, n, state[dest]) for n in out[dest]])

    return hi_pulses, lo_pulses


hi_count = 0
lo_count = 0
for i in range(1000):
    hi, lo = push()
    hi_count += hi
    lo_count += lo

print(hi_count * lo_count)
