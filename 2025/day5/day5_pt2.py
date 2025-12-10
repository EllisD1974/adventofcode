# Day 5 - Part 1
from typing import List, Tuple, Union, Any, Set


def get_puzzle_input(input_file: str = None) -> List[str]:
    """Read in the puzzle input file into a list."""
    input_file = input_file or "puzzle_input.txt"
    with open(input_file, "r") as f:
        return [line.strip() for line in f]

def split_puzzle_input(puzzle_input: List[str]) -> Tuple[List[Union[tuple, Any]], List[str]]:
    """Split up the input into two separate lists."""
    ranges, available = [], []
    use_other = False

    for line in puzzle_input:
        if line == "":
            use_other = True
            continue
        if use_other:
            available.append(int(line))
        else:
            split_list = [int(v) for v in line.split("-")]
            ranges.append(split_list)

    return ranges, available

def count_unique_numbers(ranges: List[List[int]]) -> int:
    """Get the number of unique numbers given a list of ranges."""
    # Sort ranges by start value
    ranges = sorted(ranges)

    merged = []
    for mn, mx in ranges:
        if not merged or mn > merged[-1][1] + 1:
            merged.append([mn, mx])
        else:
            merged[-1][1] = max(merged[-1][1], mx)

    # Count unique values covered
    return sum(mx - mn + 1 for mn, mx in merged)

def calculate_password(ranges: List[List[int]], available: List[int]) -> int:
    """Calculate the password."""
    return count_unique_numbers(ranges)

if __name__ == "__main__":
    puzzle_input = get_puzzle_input()
    # puzzle_input = get_puzzle_input("test_puzzle_input_ex.txt")
    ranges, available = split_puzzle_input(puzzle_input)

    password = calculate_password(ranges, available)

    print(f"{password=}")
