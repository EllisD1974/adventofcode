from typing import List

LEFT_CHAR = "L"
RIGHT_CHAR = "R"
DIAL_START = 50
DIAL_MIN = 0    # Inclusive
DIAL_MAX = 99   # Inclusive


def get_puzzle_input() -> List[str]:
    """Read in the puzzle input file into a list."""
    with open("puzzle_input.txt", "r") as f:
        return [line.strip() for line in f]

def rotate_dial(dial_val: int, rotate_key: str) -> int:
    """Return the dial value after a single rotation."""
    rot_amount = int(rotate_key[1:])    # Chop off L or R character from start of key

    if rotate_key.startswith(LEFT_CHAR):
        return (dial_val - rot_amount) % 100
    else:
        return (dial_val + rot_amount) % 100

def calculate_password(puzzle_input: List[str], dial_start: int) -> int:
    """Calculate the whole password given the input list and dial start value."""
    current_dial_val = dial_start
    zero_count = 0
    for input in puzzle_input:
        current_dial_val = rotate_dial(current_dial_val, input)
        if current_dial_val == 0:
            zero_count += 1
    return zero_count

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    password = calculate_password(puzzle_input, DIAL_START)

    print(f"{password=}")
