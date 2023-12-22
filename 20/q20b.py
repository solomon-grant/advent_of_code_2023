import itertools
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
    q = deque([("broadcaster", n, LO) for n in out["broadcaster"]])
    while q:
        src, dest, pulse = q.popleft()
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


# for i in range(3876):
#     push()
#     s = f"{state['qb']}{state['gf']}{state['kc']}{state['ps']}{state['hd']}{state['kq']}{state['cr']}{state['hm']}{state['dv']}{state['qf']}{state['ks']}{state['vd']}"
#     print(s)
# push()
# s = f"{state['qb']}{state['gf']}{state['kc']}{state['ps']}{state['hd']}{state['kq']}{state['cr']}{state['hm']}{state['dv']}{state['qf']}{state['ks']}{state['vd']}"
# print(s)
cycles = []
for root in out["broadcaster"]:
    n = root
    d = [n]
    next_ = [x for x in out[n] if t[x] == "%"]
    while next_:
        n = next_[0]
        d.append(n)
        next_ = [x for x in out[n] if t[x] == "%"]

    print(root)
    cycles.append(sum(2**i for i, y in enumerate(d) if any(t[z] == "&" for z in out[y])))

print(cycles)
print(cycles[0] * cycles[1] * cycles[2] * cycles[3])
