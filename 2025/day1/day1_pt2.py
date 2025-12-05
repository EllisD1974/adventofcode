from typing import List, Union

LEFT_CHAR = "L"
RIGHT_CHAR = "R"
DIAL_START = 50
DIAL_MAX = 99   # Inclusive


def get_puzzle_input(input_file: str = None) -> List[str]:
    """Read in the puzzle input file into a list."""
    input_file = input_file or "puzzle_input.txt"
    with open(input_file, "r") as f:
        return [line.strip() for line in f]

def rotate_dial(dial_val: int, rotate_key: str):
    """Return the dial value after a single rotation."""
    rot_amount = int(rotate_key[1:])  # Chop off L or R character from start of key

    # Make rot_amount negative if left rotation
    if rotate_key.startswith(LEFT_CHAR):
        rot_amount *= -1

    new_dial_val_not_wrapped = dial_val + rot_amount
    new_dial_val = new_dial_val_not_wrapped % (DIAL_MAX + 1)
    num_times_passed_zero = 0

    num_times_passed_zero += abs((new_dial_val_not_wrapped // 100) - (dial_val // 100))

    if rotate_key.startswith(LEFT_CHAR):
        if new_dial_val_not_wrapped % 100 == 0:
            num_times_passed_zero += 1
        if dial_val % 100 == 0:
            num_times_passed_zero -= 1

    return new_dial_val, num_times_passed_zero

def calculate_password(puzzle_input: List[str], dial_start: int) -> int:
    """Calculate the whole password given the input list and dial start value."""
    current_dial_val = dial_start
    zero_count = 0
    for input in puzzle_input:
        current_dial_val, crossed_zero_times = rotate_dial(current_dial_val, input)
        zero_count += crossed_zero_times
    return zero_count

if __name__ == "__main__":
    # puzzle_input = get_puzzle_input("testing_puzzle_input_unofficial.txt")
    # puzzle_input = get_puzzle_input("testing_puzzle_input_provided.txt")
    puzzle_input = get_puzzle_input()

    password = calculate_password(puzzle_input, DIAL_START)

    print(f"{password=}")
