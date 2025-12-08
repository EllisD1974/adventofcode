# Day 3 - Part 1
from typing import List, Tuple

def get_puzzle_input(input_file: str = None) -> List[str]:
    """Read in the puzzle input file into a list."""
    input_file = input_file or "puzzle_input.txt"
    with open(input_file, "r") as f:
        return [line.strip() for line in f]

def get_largest_number_as_char(text: str, allow_at_end: bool = False) -> Tuple[int, int]:
    """Given some string of integers, get the largest number"""

    # Chop of the last character if we don't want that to be an option
    if not allow_at_end:
        text = text[:-1]

    largest_number = None
    largest_number_index = None

    for i, char in enumerate(text):
        num = int(char)
        if largest_number and num > largest_number:
            largest_number = num
            largest_number_index = i
        elif not largest_number:
            largest_number = num
            largest_number_index = i

    return text[largest_number_index], largest_number_index

def get_largest_joltage(text: str) -> int:
    """Given some string of integers, get the largest 'joltage'"""
    first_char, first_char_index = get_largest_number_as_char(text, allow_at_end=False)
    second_char, _ = get_largest_number_as_char(text[first_char_index + 1:], allow_at_end=True)

    return int(first_char + second_char)

def calculate_password(puzzle_input: List[str]) -> int:
    """Go through all lines of the input and output the password."""
    password = 0
    for bank in puzzle_input:
        password += get_largest_joltage(bank)

    return password

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()
    # puzzle_input = get_puzzle_input("test_puzzle_input_ex.txt")

    password = calculate_password(puzzle_input)

    print(f"{password=}")
