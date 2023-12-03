import time

def main():
    puzzle_input = open("D:\python projects\AdventOfCode2023\day3\puzzle_input.txt", "r", encoding="utf8").readlines()
    new_puzzle = []
    suma = 0

    for line in puzzle_input:
        new_puzzle.append(list(line.strip()))

    for line_nr, line in enumerate(puzzle_input):
        line = line.strip()
        for char_nr, char in enumerate(line):
            a = 1
            if not char.isdigit() and char != ".":
                for y in range(line_nr-1, line_nr+2):
                    print("symbol x", char_nr)
                    for x in range(char_nr-1, char_nr+2):
                        print("starting x", x)
                        if a > 1:
                            a -= 1
                            continue
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

    for y in new_puzzle:
        xxx = ""
        for x in y:
            xxx += x
        print(xxx)
    print(suma)


if __name__ == "__main__":
    main()
