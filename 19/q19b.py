with open("input.txt") as fp:
    content = fp.read()

workflows, parts = content.split("\n\n")
workflows = [wf.strip() for wf in workflows.split()]

WF = dict()
for wf in workflows:
    i = wf.find("{")
    name = wf[:i]
    rules = wf[i+1:len(wf)-1].split(",")
    WF[name] = rules


def make_rule(rule_str):
    if ":" in rule_str:
        cond, ret = rule_str.split(":")
        field = cond[0]
        comp = cond[1]
        val = int(cond[2:])
        if comp == ">":
            def rule_func_gt(p):
                start, end = p[field]
                if end <= val + 1:
                    match = None
                    rest = p
                elif start > val:
                    match = p
                    rest = None
                else:
                    match = {k: v for k, v in p.items()}
                    match[field] = (val + 1, end)
                    rest = {k: v for k, v in p.items()}
                    rest[field] = (start, val + 1)
                return ret, match, rest
            return rule_func_gt
        elif comp == "<":
            def rule_func_lt(p):
                start, end = p[field]
                if end <= val:
                    match = p
                    rest = None
                elif start >= val:
                    match = None
                    rest = p
                else:
                    match = {k: v for k, v in p.items()}
                    match[field] = (start, val)
                    rest = {k: v for k, v in p.items()}
                    rest[field] = (val, end)
                return ret, match, rest
            return rule_func_lt
    else:
        return lambda p: (rule_str, p, None)


def make_workflow(rules):
    funcs = [make_rule(rule) for rule in rules]

    def f(p):
        processed = []
        unmatched = p
        for func in funcs:
            if unmatched is None:
                break
            next_wf, match, rest = func(unmatched)
            if match is not None:
                processed.append((next_wf, match))
            unmatched = rest
        return processed

    return f


for name, rules in WF.items():
    WF[name] = make_workflow(rules)


total = 0
jobs = [("in", {"x": (1, 4001), "m": (1, 4001), "a": (1, 4001), "s": (1, 4001)})]
while jobs:
    wf, part = jobs.pop()
    if wf == "A":
        total += (part["x"][1] - part["x"][0]) * (part["m"][1] - part["m"][0]) * (part["a"][1] - part["a"][0]) * (part["s"][1] - part["s"][0])
    elif wf == "R":
        continue
    else:
        jobs.extend(WF[wf](part))
print(total)
