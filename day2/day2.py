from dataclasses import dataclass


@dataclass
class Colors:
    red = "red"
    green = "green"
    blue = "blue"


def main():
    puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()

    max_red = 12
    max_green = 13
    max_blue = 14

    suma = 0
    points = 0
    for line in puzzle_input:
        line = line.strip()

        min_red = 0
        min_green = 0
        min_blue = 0

        game_valid = True
        game_nr, matches = line.split(": ")
        game_nr = int(game_nr.split(" ")[1])

        for match in matches.split("; "):
            respective_squares = match.split(", ")
            for square_info in respective_squares:
                amount_of_squares, square_color = square_info.split(" ")
                amount_of_squares = int(amount_of_squares)

                if square_color == Colors.red:
                    if amount_of_squares > max_red:
                        game_valid = False
                    if amount_of_squares > min_red:
                        min_red = amount_of_squares

                elif square_color == Colors.green:
                    if amount_of_squares > max_green:
                        game_valid = False
                    if amount_of_squares > min_green:
                        min_green = amount_of_squares

                elif square_color == Colors.blue:
                    if amount_of_squares > max_blue:
                        game_valid = False
                    if amount_of_squares > min_blue:
                        min_blue = amount_of_squares
        if game_valid:
            suma += game_nr
        points += (min_red*min_green*min_blue)
    print("part one answer:", suma)
    print("part two answer:", points)


if __name__ == "__main__":
    main()