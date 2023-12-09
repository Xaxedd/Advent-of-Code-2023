def part_one_answer(times, distances):
    races = []
    for i in range(len(times)):
        races.append([times[i], distances[i]])

    print("part one answer:", race_answer(races))


def part_two_answer(times, distances):
    one_time = ""
    for time in times:
        one_time += str(time)

    one_distance = ""
    for distance in distances:
        one_distance += str(distance)

    print("part two answer:", race_answer([[int(one_time), int(one_distance)]]))


def race_answer(races):
    list_good_races = []
    for race in races:
        good_race = 0
        for i in range(0, race[0] + 1):
            seconds_to_move = race[0] - i
            distance_travelled = i * seconds_to_move
            if distance_travelled > race[1]:
                good_race += 1
        list_good_races.append(good_race)
    suma = 1
    for x in list_good_races:
        suma = suma * x
    return suma


if __name__ == "__main__":
    puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()
    times = [int(x) for x in puzzle_input[0].strip().split("Time:")[1].split(" ") if x != ""]
    distances = [int(x) for x in puzzle_input[1].strip().split("Distance:")[1].split(" ") if x != ""]

    part_one_answer(times, distances)
    part_two_answer(times, distances)
