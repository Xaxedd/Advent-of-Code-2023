import matplotlib.pyplot as plt
import numpy as np

puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()

tiles = {
    "|": [[1, 0, 1],
          [1, 0, 1],
          [1, 0, 1]],

    "-": [[1, 1, 1],
          [0, 0, 0],
          [1, 1, 1]],

    "L": [[1, 0, 1],
          [1, 0, 0],
          [1, 1, 1]],

    "J": [[1, 0, 1],
          [0, 0, 1],
          [1, 1, 1]],

    "7": [[1, 1, 1],
          [0, 0, 1],
          [1, 0, 1]],

    "F": [[1, 1, 1],
          [1, 0, 0],
          [1, 0, 1]],

    ".": [[1, 1, 1],
          [1, 1, 1],
          [1, 1, 1]],

    "S": [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]],
}

maze = []
print(maze)

for index_y, line in enumerate(puzzle_input):
    line = line.strip()
    maze.append([])
    maze.append([])
    maze.append([])
    for index_x, char in enumerate(line):
        char_tile = tiles[char]
        for i, row in enumerate(char_tile):
            maze[index_y*3+i].extend(row)
print(len(maze), len(maze[0]))

maze_map = np.array(maze)

print(maze_map)

plt.gca().set_aspect('equal')
plt.gca().invert_yaxis()
plt.pcolormesh(maze_map, cmap="Greys")
plt.show()