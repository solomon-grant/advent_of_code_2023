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


def make_func(rule):
    if ":" in rule:
        cond, ret = rule.split(":")
        field = cond[0]
        comp = cond[1]
        val = int(cond[2:])
        if comp == ">":
            return lambda p: ret if p[field] > val else ""
        elif comp == "<":
            return lambda p: ret if p[field] < val else ""
    else:
        return lambda p: rule


def make_make_func(rules):
    funcs = [make_func(rule) for rule in rules]

    def f(p):
        for func in funcs:
            val = func(p)
            if val:
                return val
    return f


for name, rules in WF.items():
    WF[name] = make_make_func(rules)


def parse_part(part_str):
    p = dict()
    fields = part_str[1:-1].split(",")
    for field in fields:
        k, v = field.split("=")
        p[k] = int(v)
    return p


def solve_part(p):
    wf = "in"
    while wf not in "AR":
        wf = WF[wf](p)
    return wf


parts = [parse_part(part.strip()) for part in parts.split()]
total = 0
for part in parts:
    outcome = solve_part(part)
    if outcome == "A":
        total += sum(part.values())
print(total)
