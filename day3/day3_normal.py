import time

def main():
    puzzle_input = open("D:\python projects\AdventOfCode2023\day3\puzzle_input.txt", "r", encoding="utf8").readlines()
    new_puzzle = []
    suma = 0
    gear_ratio = 0

    for line in puzzle_input:
        new_puzzle.append(list(line.strip()))

    for line_nr, line in enumerate(puzzle_input):
        line = line.strip()
        for char_nr, char in enumerate(line):
            a = 1
            if not char.isdigit() and char != ".":
                numbers_near_this_symbol = []
                for y in range(line_nr-2, line_nr+3):
                    xxx = ""
                    for x in range(char_nr-5, char_nr+7):
                        if x > len(line)-1 or y > len(new_puzzle) - 1:
                            continue
                        xxx += str(new_puzzle[y][x])
                    print(xxx)


                print(f"symbol cords: y{line_nr} x{char_nr}")
                for y in range(line_nr-1, line_nr+2):
                    a = 1
                    for x in range(char_nr-1, char_nr+2):
                        print(f"cord checking y{y} x{x}")
                        if a > 1:
                            a -= 1
                            continue
                        print(puzzle_input[y][x])
                        if puzzle_input[y][x].isdigit():
                            number = str(puzzle_input[y][x])
                            new_puzzle[y][x] = "."
                            while True:
                                if puzzle_input[y][x-a].isdigit():
                                    number = str(puzzle_input[y][x-a]) + number
                                    new_puzzle[y][x - a] = "."
                                else:
                                    break
                                a+=1

                            a = 1
                            while True:
                                if puzzle_input[y][x + a].isdigit():
                                    number = number + str(puzzle_input[y][x + a])
                                    new_puzzle[y][x + a] = "."
                                else:
                                    break
                                a += 1
                            print(number)
                            suma += int(number)
                            numbers_near_this_symbol.append(int(number))
                if char == "*":
                    if len(numbers_near_this_symbol) == 2:
                        gear_ratio += (numbers_near_this_symbol[0] * numbers_near_this_symbol[1])

                for y in range(line_nr-2, line_nr+3):
                    xxx = ""
                    for x in range(char_nr-5, char_nr+7):
                        if x > len(line)-1 or y > len(new_puzzle) - 1:
                            continue
                        xxx += str(new_puzzle[y][x])

                    print(xxx)
                print("\n"*2)

    for y in new_puzzle:
        xxx = ""
        for x in y:
            xxx += x
        print(xxx)
    print("part one answer:", suma)
    print("part two answer:", gear_ratio)


if __name__ == "__main__":
    main()
