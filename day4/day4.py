puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()

points = 0
card_amount_of_winning_numbers = {}
amount_of_cards = {}
for i in range(1, len(puzzle_input) + 1):
    amount_of_cards[str(i)] = 1

for index, line in enumerate(puzzle_input):
    line = line.strip()
    scratch_card_numbers = line.split(": ")[1]

    winning_numbers = [x for x in scratch_card_numbers.split(" | ")[0].split(" ") if x != ""]
    numbers_you_have = [x for x in scratch_card_numbers.split(" | ")[1].split(" ") if x != ""]

    winning_numbers_found = 0
    for number in numbers_you_have:
        if number in winning_numbers:
            if winning_numbers_found == 0:
                points += 1
            else:
                points += 1 * pow(2, winning_numbers_found - 1)
            winning_numbers_found += 1
    card_amount_of_winning_numbers[str(index + 1)] = winning_numbers_found
print("part one answer:", points)

for card_nr, amnt_of_card in amount_of_cards.items():
    print(card_nr)
    for i in range(amnt_of_card):
        for j in range(card_amount_of_winning_numbers[card_nr]):
            amount_of_cards[str(int(card_nr) + j + 1)] += 1

sum_of_cards = sum(x for x in amount_of_cards.values())
print("part two answer:", sum_of_cards)
