def part_one_answer(trees):
    suma = 0
    for tree in trees:
        for layer in tree:
            suma += layer[0]
    print(f"part one answer: {suma}")


def part_two_answer(trees):
    suma = 0
    for tree in trees:
        first_value = tree[-1][0]
        for layer in reversed(tree):
            first_value = layer[0] - first_value
        suma += first_value
    print(f"part two answer: {suma}")


def get_trees(puzzle_input):
    trees = []
    for line in puzzle_input:
        line = line.strip()

        tree = []
        tree.append([int(x) for x in line.split(" ")])

        for layer in tree:
            next_layer = []

            i = 0
            while i < len(layer) - 1:
                skip = layer[i + 1] - layer[i]
                next_layer.append(skip)
                i += 1
            tree.append(next_layer)

            all_zeroes = True
            for value in next_layer:
                if value != 0:
                    all_zeroes = False
            if all_zeroes:
                break

        trees.append(tree)
    return trees


if __name__ == "__main__":
    puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()

    trees = get_trees(puzzle_input)
    part_one_answer(trees)
    part_two_answer(trees)