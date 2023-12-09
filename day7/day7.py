from dataclasses import dataclass
from enum import Enum
from typing import List


class PART(Enum):
    ONE = 0,
    TWO = 1


class HandType(Enum):
    FIVE_OF_KIND = 6
    FOUR_OF_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_KIND = 3
    TWO_PAIRS = 2
    ONE_PAIR = 1
    HIGH_CARD = 0


@dataclass
class PokerHand:
    points: int
    cards: str
    type: HandType = None
    rank: int = None


def puzzle_answer(puzzle_input, part: PART):
    hand_list = []
    for line in puzzle_input:
        line = line.strip()
        hand_list.append(PokerHand(points=int(line.split(" ")[1]), cards=line.split(" ")[0]))

    hands_dict = assign_card_types(hand_list, part)
    ranked_cards = sort_cards_by_rank(hands_dict, part)

    suma = 0
    for hand in ranked_cards:
        suma += hand.points * hand.rank
    print(f"part {part.name.lower()} answer: {suma}")


def assign_card_types(hand_list, part):
    if part is PART.ONE:
        return part_one_card_type_assign(hand_list)
    else:
        return part_two_card_type_assign(hand_list)


def sort_cards_by_rank(hands_dict, part):
    rank = 0
    ranked_cards = []
    for key, value in hands_dict.items():
        rank += 1
        if len(value) == 1:
            ranked_cards.extend(value)
            continue

        if part is PART.ONE:
            ranked_cards.extend(rank_cards(value, part=PART.ONE))
        else:
            ranked_cards.extend(rank_cards(value, part=PART.TWO))

        for index, hand in enumerate(reversed(ranked_cards), start=1):
            hand.rank = index
    return ranked_cards


def rank_cards(list_of_hands: List[PokerHand], part: PART):
    card_values = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2
    }

    if part is PART.TWO:
        card_values["J"] = 1

    ranked = []
    while len(list_of_hands) > 0:
        max_card = list_of_hands[0]
        for hand in list_of_hands:
            for i in range(5):
                if card_values[hand.cards[i]] > card_values[max_card.cards[i]]:
                    max_card = hand
                    break
                elif card_values[hand.cards[i]] == card_values[max_card.cards[i]]:
                    continue
                else:
                    break
        ranked.append(max_card)
        list_of_hands.pop(list_of_hands.index(max_card))
    return ranked


def part_one_card_type_assign(hand_list):
    hands_dict = {
        "FIVE_OF_KIND": [],
        "FOUR_OF_KIND": [],
        "FULL_HOUSE": [],
        "THREE_OF_KIND": [],
        "TWO_PAIRS": [],
        "ONE_PAIR": [],
        "HIGH_CARD": [],
    }

    for hand in hand_list:
        cards_found = {
            "A": 0,
            "K": 0,
            "Q": 0,
            "J": 0,
            "T": 0,
            "9": 0,
            "8": 0,
            "7": 0,
            "6": 0,
            "5": 0,
            "4": 0,
            "3": 0,
            "2": 0
        }
        for card in hand.cards:
            cards_found[card] += 1

        cards_sorted = list(reversed(sorted(cards_found.values())))
        if cards_sorted[0] == 5:
            hand.type = HandType.FIVE_OF_KIND
        elif cards_sorted[0] == 4:
            hand.type = HandType.FOUR_OF_KIND
        elif cards_sorted[0] == 3 and cards_sorted[1] == 2:
            hand.type = HandType.FULL_HOUSE
        elif cards_sorted[0] == 3:
            hand.type = HandType.THREE_OF_KIND
        elif cards_sorted[0] == 2 and cards_sorted[1] == 2:
            hand.type = HandType.TWO_PAIRS
        elif cards_sorted[0] == 2 and cards_sorted[1] == 1:
            hand.type = HandType.ONE_PAIR
        else:
            hand.type = HandType.HIGH_CARD

        hands_dict[hand.type.name].append(hand)
    return hands_dict


def part_two_card_type_assign(hand_list):
    hands_dict = {
        "FIVE_OF_KIND": [],
        "FOUR_OF_KIND": [],
        "FULL_HOUSE": [],
        "THREE_OF_KIND": [],
        "TWO_PAIRS": [],
        "ONE_PAIR": [],
        "HIGH_CARD": [],
    }

    for hand in hand_list:
        cards_found = {
            "A": 0,
            "K": 0,
            "Q": 0,
            "J": 0,
            "T": 0,
            "9": 0,
            "8": 0,
            "7": 0,
            "6": 0,
            "5": 0,
            "4": 0,
            "3": 0,
            "2": 0
        }
        for card in hand.cards:
            cards_found[card] += 1

        jokers_amount = cards_found["J"]
        cards_found["J"] = 0
        cards_sorted = list(reversed(sorted(cards_found.values())))

        if cards_sorted[0] + jokers_amount == 5:
            hand.type = HandType.FIVE_OF_KIND
        elif cards_sorted[0] + jokers_amount == 4:
            hand.type = HandType.FOUR_OF_KIND
        elif cards_sorted[0] + jokers_amount == 3 and cards_sorted[1] == 2:
            hand.type = HandType.FULL_HOUSE
        elif cards_sorted[0] + jokers_amount == 3:
            hand.type = HandType.THREE_OF_KIND
        elif cards_sorted[0] + jokers_amount == 2 and cards_sorted[1] == 2:
            hand.type = HandType.TWO_PAIRS
        elif cards_sorted[0] + jokers_amount == 2 and cards_sorted[1] == 1:
            hand.type = HandType.ONE_PAIR
        else:
            hand.type = HandType.HIGH_CARD

        hands_dict[hand.type.name].append(hand)
    return hands_dict


if __name__ == "__main__":
    puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()

    puzzle_answer(puzzle_input, PART.ONE)
    puzzle_answer(puzzle_input, PART.TWO)
