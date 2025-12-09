# Day 4 - Part 1
from typing import List
import numpy as np


EMPTY = "."
FULL = "@"


def get_puzzle_input(input_file: str = None) -> np.array([List[str]]):
    """Read in the puzzle input file into a numpy matrix."""
    input_file = input_file or "puzzle_input.txt"
    with open(input_file) as f:
        return np.array([list(line.strip()) for line in f])

def get_chip(matrix: np.array([List[str]]), x: int, y: int) -> List[List[str]]:
    """Get a 'chip', i.e a 3x3 matrix of values surrounding and including the current coordinates."""
    x1 = max(0, x - 1)
    x2 = min(matrix.shape[0], x + 2)
    y1 = max(0, y - 1)
    y2 = min(matrix.shape[1], y + 2)
    return matrix[y1:y2, x1:x2]

def check_for_n_adjacent_chars(puzzle_input: np.array([List[str]]), x: int, y: int , max_allowed_full_neighbors: int = 4 - 1):
    """Check if there are under the max allowed number of adjacent neighboring values that are not full."""
    current_char = puzzle_input[y][x]
    if current_char == FULL:
        chip = get_chip(puzzle_input, x, y)
        if np.count_nonzero(chip == FULL) - 1 <= max_allowed_full_neighbors:
            return True
    return False

def calculate_password(puzzle_input: np.array([List[str]])) -> int:
    """Calculate password."""
    password = 0
    pass_modified = True

    # Loop over the matrix as many times as needed until no more changes are made
    while pass_modified:
        pass_modified = False
        for y in range(len(puzzle_input)):
            for x in range(len(puzzle_input[y])):
                if check_for_n_adjacent_chars(puzzle_input, x, y):
                    password += 1

                    # Clear the current spot
                    puzzle_input[y][x] = EMPTY

                    pass_modified = True
    return password


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()
    # puzzle_input = get_puzzle_input("test_puzzle_input_ex.txt")

    password = calculate_password(puzzle_input)

    print(f"{password=}")
