import math

with open("input.txt") as fp:
    race_times = list(map(int, fp.readline().split(":")[1].strip().split()))
    records = list(map(int, fp.readline().split(":")[1].strip().split()))

    def ways_to_win(race):
        T, R = race
        return 2 * math.floor(math.sqrt(T**2 / 4 - R)) + 1 - T % 2

    print(math.prod(map(ways_to_win, zip(race_times, records))))
