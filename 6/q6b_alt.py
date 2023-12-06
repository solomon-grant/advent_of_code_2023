import math

with open("input.txt") as fp:
    race_time = int("".join(fp.readline().split(":")[1].strip().split()))
    record = int("".join(fp.readline().split(":")[1].strip().split()))

    def ways_to_win(T, R):
        return 2 * math.floor(math.sqrt(T**2 / 4 - R)) + 1 - T % 2

    print(ways_to_win(race_time, record))