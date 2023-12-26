import math
from enum import Enum
from typing import List

import matplotlib.pyplot as plt
import numpy as np
from numpy import ndarray


class Direction(Enum):
    UP = 0,
    DOWN = 1,
    LEFT = 2,
    RIGHT = 3


def generate_maze_map(puzzle_input) -> ndarray:
    maze = []
    for index_y, line in enumerate(puzzle_input):
        line = line.strip()
        maze.append([])
        maze.append([])
        maze.append([])
        for index_x, char in enumerate(line):
            char_tile = tile_types[char]
            for i, row in enumerate(char_tile):
                maze[index_y * 3 + i].extend(row)
    maze_map = np.array(maze)
    return maze_map


def get_starting_position(puzzle_input) -> dict:
    for index_y, line in enumerate(puzzle_input):
        for index_x, char in enumerate(line):
            if char == "S":
                return {"y": index_y * 3 + 1, "x": index_x * 3 + 1}


def draw_maze_loop_and_get_amount_of_steps_taken(maze_map, starting_position):
    current_position = starting_position
    steps_taken = 0
    while True:
        if is_space_free(current_position, maze_map, Direction.UP):
            maze_map[current_position["y"] - 1][current_position["x"]] = 8
            current_position["y"] -= 1

        elif is_space_free(current_position, maze_map, Direction.DOWN):
            maze_map[current_position["y"] + 1][current_position["x"]] = 8
            current_position["y"] += 1

        elif is_space_free(current_position, maze_map, Direction.LEFT):
            maze_map[current_position["y"]][current_position["x"] - 1] = 8
            current_position["x"] -= 1

        elif is_space_free(current_position, maze_map, Direction.RIGHT):
            maze_map[current_position["y"]][current_position["x"] + 1] = 8
            current_position["x"] += 1

        elif current_position["y"] == starting_position["y"] and current_position["x"] == starting_position["x"]:
            break

        steps_taken += 1

    return maze_map, steps_taken


def is_space_free(current_position, maze_map, direction: Direction) -> bool:
    if direction is Direction.UP:
        if maze_map[current_position["y"] - 1][current_position["x"]] == 0:
            return True

    elif direction is Direction.DOWN:
        if maze_map[current_position["y"] + 1][current_position["x"]] == 0:
            return True

    elif direction is Direction.LEFT:
        if maze_map[current_position["y"]][current_position["x"] - 1] == 0:
            return True

    elif direction is Direction.RIGHT:
        if maze_map[current_position["y"]][current_position["x"] + 1] == 0:
            return True

    return False


def delete_unused_pipes_from_maze(maze_map) -> ndarray:
    for index_y, y in enumerate(maze_map):  # change unused pipes to empty spaces
        for index_x, x in enumerate(y):
            if x == 1:
                maze_map[index_y, index_x] = 0

    return maze_map


def flood_map(maze_map: ndarray) -> ndarray:
    if maze_map[0, 0] == 0:
        maze_map[0, 0] = 3

    wave_coordinates = list(zip(*np.where(maze_map == 3)))
    while len(wave_coordinates) != 0:
        wave_coordinates = list(zip(*np.where(maze_map == 3)))
        for coordinates in wave_coordinates:
            current_flood_position = {"y": coordinates[0], "x": coordinates[1]}
            try:
                if is_space_free(current_flood_position, maze_map, Direction.UP):
                    maze_map[current_flood_position["y"] - 1][current_flood_position["x"]] = 3
            except:
                pass
            try:
                if is_space_free(current_flood_position, maze_map, Direction.DOWN):
                    maze_map[current_flood_position["y"] + 1][current_flood_position["x"]] = 3
            except:
                pass
            try:
                if is_space_free(current_flood_position, maze_map, Direction.LEFT):
                    maze_map[current_flood_position["y"]][current_flood_position["x"] - 1] = 3
            except:
                pass
            try:
                if is_space_free(current_flood_position, maze_map, Direction.RIGHT):
                    maze_map[current_flood_position["y"]][current_flood_position["x"] + 1] = 3
            except:
                pass

            maze_map[current_flood_position["y"]][current_flood_position["x"]] = 4

    return maze_map


def slice_maze_map_into_3x3_tiles(maze_map) -> List[List[List[int]]]:
    maze_tiles = []
    for y in range(0, len(maze_map), 3):
        for x in range(0, len(maze_map[0]), 3):
            maze_tiles.append([[maze_map[y][x], maze_map[y][x + 1], maze_map[y][x + 2]],
                               [maze_map[y + 1][x], maze_map[y + 1][x + 1], maze_map[y + 1][x + 2]],
                               [maze_map[y + 2][x], maze_map[y + 2][x + 1], maze_map[y + 2][x + 2]]])
    return maze_tiles


def get_amount_of_enclosed_tiles(maze_tiles) -> int:
    tiles_enclosed = 0
    for tile in maze_tiles:
        tile_empty = True
        for line in tile:
            for cord in line:
                if cord != 0:
                    tile_empty = False

        if tile_empty:
            tiles_enclosed += 1
    return tiles_enclosed


def generate_map_visualization(map) -> None:
    plt.gca().set_aspect('equal')
    plt.gca().invert_yaxis()
    plt.pcolormesh(map, cmap="rainbow")
    plt.show()


tile_types = {
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

    "S": [[1, 0, 1],
          [0, 0, 1],
          [1, 1, 1]],
}


if __name__ == "__main__":
    puzzle_input = open("puzzle_input.txt", "r", encoding="utf8").readlines()

    maze_map = generate_maze_map(puzzle_input)
    starting_position = get_starting_position(puzzle_input)
    maze_map, steps_taken = draw_maze_loop_and_get_amount_of_steps_taken(maze_map, starting_position)

    print("part one answer:", math.ceil(int((steps_taken / 3) / 2)))

    maze_map = delete_unused_pipes_from_maze(maze_map)
    flooded_map = flood_map(maze_map)
    maze_tiles = slice_maze_map_into_3x3_tiles(flooded_map)
    tiles_enclosed = get_amount_of_enclosed_tiles(maze_tiles)

    print("part two answer:", tiles_enclosed)

    generate_map_visualization(flooded_map)
