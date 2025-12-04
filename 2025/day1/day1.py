
from typing import List

LEFT_CHAR = "L"
RIGHT_CHAR = "R"
DIAL_START = 50
DIAL_MIN = 0    # Inclusive
DIAL_MAX = 99   # Inclusive


def get_puzzle_input() -> List[str]:
    with open("puzzle_input.txt", "r") as f:
        return [line.strip() for line in f]

def rotate_dial(dial_val: int, rotate_key: str) -> int:
    rot_amount = int(rotate_key[1:])

    if rotate_key.startswith(LEFT_CHAR):
        return (dial_val - rot_amount) % 100
    else:
        return (dial_val + rot_amount) % 100

def calculate_password(puzzle_input: List[str]) -> int:
    current_dial_val = DIAL_START
    zero_count = 0
    for input in puzzle_input:
        current_dial_val = rotate_dial(current_dial_val, input)
        if current_dial_val == 0:
            zero_count += 1
    return zero_count

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    password = calculate_password(puzzle_input)

    print(f"{password=}")