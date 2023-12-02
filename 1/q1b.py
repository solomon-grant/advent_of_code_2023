import re


def toint(string):
    if string in "123456789":
        return int(string)
    elif string == "one":
        return 1
    elif string == "two":
        return 2
    elif string == "three":
        return 3
    elif string == "four":
        return 4
    elif string == "five":
        return 5
    elif string == "six":
        return 6
    elif string == "seven":
        return 7
    elif string == "eight":
        return 8
    else:
        return 9


fwd_pattern = re.compile("\d|one|two|three|four|five|six|seven|eight|nine")
rev_pattern = re.compile("\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin")
with open("input.txt") as fp:
    print(sum(10 * toint(fwd_pattern.search(line)[0]) + toint(rev_pattern.search(line[::-1])[0][::-1]) for line in fp))
