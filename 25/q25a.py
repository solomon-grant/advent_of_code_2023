import collections
import itertools
import sys


def reachable(adj, root):
    r = set()
    stack = [root]
    while stack:
        v = stack.pop()
        if v in r:
            continue
        r.add(v)
        for o in adj[v]:
            stack.append(o)
    return r


def find_bridge(adj, root):
    bridge = None
    seen = dict()
    low = dict()
    parent = {root: None}

    time = 0

    def dfs_vlow(v):
        nonlocal time
        nonlocal bridge

        time += 1
        seen[v] = time
        low[v] = time
        for x in adj[v]:
            if x not in seen:
                parent[x] = v
                dfs_vlow(x)
                low[v] = min(low[v], low[x])
                if low[x] > seen[v]:
                    bridge = (x, v) if x < v else (v, x)
            elif x != parent[v]:
                low[v] = min(low[v], seen[x])

    dfs_vlow(root)
    return bridge


if __name__ == "__main__":
    sys.setrecursionlimit(10000)

    adj = collections.defaultdict(set)
    vertices = set()
    edges = set()
    root = ""
    with open("input.txt") as fp:
        for line in fp.readlines():
            v, others = line.split(": ")
            if not root:
                root = v
            vertices.add(v)
            for other in others.split():
                vertices.add(other)
                edges.add((v, other) if v < other else (other, v))
                adj[v].add(other)
                adj[other].add(v)

    counter = 0
    for (v1, v2), (v3, v4) in itertools.combinations(edges, 2):
        counter += 1
        if counter % 1000 == 0:
            print(counter)

        adj[v1].remove(v2)
        adj[v2].remove(v1)
        adj[v3].remove(v4)
        adj[v4].remove(v3)

        b = find_bridge(adj, root)
        if b is not None:
            b1, b2 = b
            adj[b1].remove(b2)
            adj[b2].remove(b1)
            r = reachable(adj, root)
            print(len(r) * len(vertices - r))
            break

        adj[v1].add(v2)
        adj[v2].add(v1)
        adj[v3].add(v4)
        adj[v4].add(v3)



