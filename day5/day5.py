import time


def part_one(puzzle_input):
    seeds = [int(x) for x in puzzle_input[0].split(": ")[1].strip().split(" ")]

    all_converts = get_all_maps_converted(puzzle_input)

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
    print("part one answer:", seed_to_location[0])


def part_two(puzzle_input):
    seeds = [int(x) for x in puzzle_input[0].split(": ")[1].strip().split(" ")]
    seed_ranges = []
    temp = []
    for seed in seeds:
        temp.append(seed)
        if len(temp) == 2:
            seed_ranges.append(temp)
            temp = []

    print(seed_ranges)
    all_converts = get_all_maps_converted(puzzle_input)
    for crop_map in all_converts:
        for seed_range in seed_ranges:
            for crop_range in crop_map:
                if crop_range[1] <= seed_range[0] and (crop_range[1] + crop_range[2]) >= (seed_range[0] + seed_range[1]):  # range in range
                    amount_to_add = seed_range[0] - crop_range[1]
                    seed_range[0] = crop_range[0] + amount_to_add
                    break

                elif crop_range[1] <= seed_range[0] < (crop_range[1] + crop_range[2]):  # range ends higher    --->|--
                    exceeded_amount = seed_range[0] + seed_range[1] - (crop_range[1] + crop_range[2])
                    exceeded_start = seed_range[0] + seed_range[1] - exceeded_amount
                    seed_ranges.append([exceeded_start, exceeded_amount])  # |--
                    seed_range[1] = seed_range[1] - exceeded_amount
                    seed_range[0] = seed_range[0] - crop_range[1] + crop_range[0]
                    break

                elif seed_range[0] < crop_range[1] and (
                        crop_range[1] < seed_range[0] + seed_range[1] < crop_range[1] + crop_range[2]):  # range starts lower   ---|--->
                    exceeded_amount = crop_range[1] - seed_range[0]
                    seed_ranges.append([seed_range[0], exceeded_amount])  # --->

                    seed_range[0] = crop_range[0]
                    seed_range[1] = seed_range[1] - exceeded_amount
                    break

                elif seed_range[0] < crop_range[1] + crop_range[2] < seed_range[0] + seed_range[1]:  # range overflowing from both sides ---|--->|---
                    print("range overflows")
                    left_exceeded_amount = crop_range[1] - seed_range[0] + 1
                    seed_ranges.append([seed_range[0], left_exceeded_amount])  # ---|

                    right_exceeded_amount = seed_range[0] + seed_range[1] - (crop_range[1] + crop_range[2])
                    exceeded_start = seed_range[0] + seed_range[1] - right_exceeded_amount
                    seed_ranges.append([exceeded_start, right_exceeded_amount])  # |---

                    seed_range[0] = crop_range[1]  # |-->|
                    seed_range[1] = seed_range[1] - left_exceeded_amount - right_exceeded_amount  # |-->|
                    break

        xxx = []
        for yyy in seed_ranges:
            xxx.append(yyy[0])
        xxx.sort()
        print("part two answer:", xxx[0])


def get_all_maps_converted(puzzle_input):
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
    return all_converts


if __name__ == "__main__":
    puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()

    part_one(puzzle_input)
    part_two(puzzle_input)
