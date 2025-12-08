# Day 3 - Part 1
from typing import List

def get_puzzle_input(input_file: str = None) -> List[str]:
    """Read in the puzzle input file into a list."""
    input_file = input_file or "puzzle_input.txt"
    with open(input_file, "r") as f:
        return [line.strip() for line in f]

def max_joltage(text: str, max_len: int = 12) -> int:
    """Return the max joltage value given the input string of integers and an optional max length of chars."""

    # Get the min number of numbers we have to remove in order to get to "max_len" if needed
    remove_amount = len(text) - max_len

    stack = []

    for char in text:
        digit = int(char)

        # If we have a > 0 remove amount, a stack and the last digit of the stack is less than the current digit
        while remove_amount and stack and stack[-1] < digit:
            # Remove the last digit off the stack
            stack.pop()

            # Decrement our remove_amount, this will make sure we don't remove too many
            remove_amount -= 1

        # Append to our stack of numbers
        stack.append(digit)

    # Return the final number as an int
    return int("".join(map(str, stack[:max_len])))

def calculate_password(puzzle_input: List[str]) -> int:
    """Go through all lines of the input and output the password."""
    password = 0
    for bank in puzzle_input:
        password += max_joltage(bank)

    return password

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()
    # puzzle_input = get_puzzle_input("test_puzzle_input_ex.txt")

    password = calculate_password(puzzle_input)

    print(f"{password=}")
