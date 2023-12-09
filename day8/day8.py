import math


def part_one_answer(directions, nodes):
    current_node = "AAA"

    nr_of_steps = 0
    while current_node != "ZZZ":
        for direction in directions:
            if direction == "L":
                current_node = nodes[current_node][0]
            else:
                current_node = nodes[current_node][1]
            nr_of_steps += 1
    print(f"part one asnwer: {nr_of_steps}")


def part_two_answer(directions, nodes):
    current_nodes = []
    for node in nodes:
        if node[-1] == "A":
            current_nodes.append(node)

    steps = []
    for node in current_nodes:
        end = True
        nr_of_steps = 0
        while end:
            for direction in directions:
                if direction == "L":
                    node = nodes[node][0]
                else:
                    node = nodes[node][1]
                nr_of_steps += 1

                if node[-1] == "Z":
                    steps.append(nr_of_steps)
                    end = False
    print(f"part two answer: {math.lcm(*steps)}")


def get_nodes(puzzle_input):
    nodes = {}
    for line in puzzle_input:
        line = line.strip()

        xxx = line.split(" = ")
        L_R = xxx[1].replace("(", "").replace(")", "")
        L_R = L_R.split(", ")
        nodes[xxx[0]] = L_R
    return nodes


if __name__ == "__main__":
    puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()

    directions = puzzle_input[0].strip()
    puzzle_input.pop(0)
    puzzle_input.pop(0)

    nodes = get_nodes(puzzle_input)

    part_one_answer(directions, nodes)
    part_two_answer(directions, nodes)
