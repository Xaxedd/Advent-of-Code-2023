from enum import Enum


class DAYPART(Enum):
    ONE = 0
    TWO = 1


def replace_digit_words_with_ints(puzzle_input_line):
    word_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    line = ""
    for char in puzzle_input_line:
        line += char
        for i in range(0, 9):
            line_before = line
            line = line.replace(word_numbers[i], str(i + 1))
            line = line + word_numbers[i][-1] if line != line_before else line
    return line


def get_answer(puzzle_input, puzzle_part: DAYPART):
    suma = 0
    for line in puzzle_input:
        line = line.strip()
        if puzzle_part is DAYPART.TWO:
            line = replace_digit_words_with_ints(line)
        numbers_in_line = []
        for char in line:
            if char.isdigit():
                numbers_in_line.append(char)

        number = int(numbers_in_line[0] + numbers_in_line[-1])
        suma += number

    if puzzle_part is DAYPART.ONE:
        print(f"part one answer: {suma}")
    else:
        print(f"part two answer: {suma}")


if __name__ == "__main__":
    puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()

    get_answer(puzzle_input, DAYPART.ONE)
    get_answer(puzzle_input, DAYPART.TWO)
