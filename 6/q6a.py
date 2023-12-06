import math

with open("input.txt") as fp:
    race_times = list(map(int, fp.readline().split(":")[1].strip().split()))
    records = list(map(int, fp.readline().split(":")[1].strip().split()))

    def ways_to_win(race):
        T, R = race
        return math.floor((T/2) + math.sqrt(T**2 - 4*R) / 2) - math.ceil((T/2) - math.sqrt(T**2 - 4*R) / 2) + 1

    print(math.prod(map(ways_to_win, zip(race_times, records))))
