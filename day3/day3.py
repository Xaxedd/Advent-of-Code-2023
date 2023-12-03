import time


def main():
    puzzle_input = open("D:\python projects\AdventOfCode2023\day3\puzzle_input.txt", "r", encoding="utf8").readlines()
    suma = 0
    gear_ratio = 0

    for line_nr, line in enumerate(puzzle_input):
        line = line.strip()
        for char_nr, char in enumerate(line):
            if not char.isdigit() and char != ".":
                numbers_near_this_symbol = []

                for y in range(line_nr - 1, line_nr + 2):
                    characters_to_skip = 0
                    for x in range(char_nr - 1, char_nr + 2):
                        if characters_to_skip > 0:
                            characters_to_skip -= 1
                            continue

                        if puzzle_input[y][x].isdigit():
                            number = str(puzzle_input[y][x])
                            iter = 1
                            while True:
                                if puzzle_input[y][x - iter].isdigit():
                                    number = str(puzzle_input[y][x - iter]) + number
                                else:
                                    break
                                iter += 1

                            iter = 1
                            characters_to_skip = 0
                            while True:
                                if puzzle_input[y][x + iter].isdigit():
                                    number = number + str(puzzle_input[y][x + iter])
                                else:
                                    break
                                characters_to_skip += 1
                                iter += 1

                            suma += int(number)
                            numbers_near_this_symbol.append(int(number))
                if char == "*":
                    if len(numbers_near_this_symbol) == 2:
                        gear_ratio += (numbers_near_this_symbol[0] * numbers_near_this_symbol[1])

    print("part one answer:", suma)
    print("part two answer:", gear_ratio)


if __name__ == "__main__":
    main()
