from typing import List


def get_puzzle_input(input_file: str = None) -> List[str]:
    """Read in the puzzle input file into a list."""
    input_file = input_file or "puzzle_input.txt"
    with open(input_file, "r") as f:
        return f.readline().strip().split(",")

def _get_range(min_val: int, max_val: int) -> List[str]:
    """Return a list of strings representing all numbers between the given max min (inclusive)."""
    return [str(x) for x in range(min_val, max_val + 1)]

def get_range(range_str: str) -> List[str]:
    """Return a list of strings representing all numbers between the given max min in range (inclusive)."""
    # Split up range_str to get the min and max values
    split_val = range_str.split("-")
    min_val, max_val = int(split_val[0]), int(split_val[1])

    return _get_range(min_val, max_val)

def has_repeated_pattern_at_least_twice(text: str) -> bool:
    """Return whether given text is made up entirely of a repeated pattern that happens at least twice."""
    n = len(text)

    # Try every possible pattern size, but it must repeat >= 2 times
    for size in range(1, n // 2 + 1):
        if n % size == 0:  # Pattern must perfectly tile the string
            pattern = text[:size]
            repeat_count = n // size
            if text == pattern * repeat_count and repeat_count >= 2:
                return True
    return False

def is_invalid(text: str) -> bool:
    """Check if text is considered an invalid value."""
    return has_repeated_pattern_at_least_twice(text)

def calculate_password(puzzle_input: List[str]) -> str:
    """Calculate the password for a given list of strings representing ranges."""
    password = 0
    for input_range in puzzle_input:
        range_vals = get_range(input_range)
        for val in range_vals:
            if is_invalid(val):
                password += int(val)
    return password


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()
    # puzzle_input = get_puzzle_input("test_puzzle_input.txt")
    # puzzle_input = get_puzzle_input("test_puzzle_input_pt2.txt")

    password = calculate_password(puzzle_input)

    # print(f"{password=}, {(password == 1227775554)=}")
    # print(f"{password=}, {(password == 4174379265)=}")
    print(f"{password=}")
