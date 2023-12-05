def part_one(puzzle_input):
    seeds = [int(x) for x in puzzle_input[0].split(": ")[1].strip().split(" ")]
    print(seeds)

    all_converts = []
    this_map = []
    for index, line in enumerate(puzzle_input):
        if index in range(0, 3):
            continue

        if "map" in line:
            all_converts.append(this_map)
            this_map = []
            continue

        this_map.append([int(x) for x in line.strip().split(" ") if x != ""])
        if not this_map[-1]:
            this_map.pop()
    all_converts.append(this_map)

    seed_to_location = []
    for seed in seeds:
        value_rn = seed
        for crop_map in all_converts:
            value_changed = False
            for xxx in crop_map:
                if value_rn in range(xxx[1], xxx[1] + xxx[2]):
                    yyy = value_rn - xxx[1]
                    value_rn = xxx[0] + yyy
                    value_changed = True
                if value_changed:
                    break
        seed_to_location.append(value_rn)
    seed_to_location.sort()
    print(seed_to_location)
    print(seed_to_location[0])


if __name__ == "__main__":
    puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()

    part_one(puzzle_input)
