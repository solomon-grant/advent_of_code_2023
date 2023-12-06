import math

with open("input.txt") as fp:
    race_time = int("".join(fp.readline().split(":")[1].strip().split()))
    record = int("".join(fp.readline().split(":")[1].strip().split()))

    def ways_to_win(T, R):
        return math.floor((T/2) + math.sqrt(T**2 - 4*R) / 2) - math.ceil((T/2) - math.sqrt(T**2 - 4*R) / 2) + 1

    print(ways_to_win(race_time, record))