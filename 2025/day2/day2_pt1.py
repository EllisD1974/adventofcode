from typing import List



def get_puzzle_input(input_file: str = None) -> List[str]:
    """Read in the puzzle input file into a list."""
    input_file = input_file or "puzzle_input.txt"
    with open(input_file, "r") as f:
        return f.readline().strip().split(",")

def _get_range(min_val: int, max_val: int) -> List[str]:
    return [str(x) for x in range(min_val, max_val + 1)]

def get_range(range_str: str) -> List[int]:
    # Split up range_str to get the min and max values
    split_val = range_str.split("-")
    min_val, max_val = int(split_val[0]), int(split_val[1])

    return _get_range(min_val, max_val)

def find_sequential_double_pattern(text: str) -> List[str]:
    patterns = []

    for size in range(1, len(text)//2 + 1):
        for i in range(len(text) - 2 * size + 1):
            pattern = text[i:i+size]
            next_pattern = text[i+size:i+2*size]

            if pattern == next_pattern:
                # Ensure it does NOT repeat more than twice
                third_start = i + 2 * size
                if third_start + size <= len(text) and text[third_start:third_start+size] == pattern:
                    continue  # skips if more than twice

                patterns.append(pattern)

    return patterns

def has_sequential_double_pattern(text: str) -> bool:
    for size in range(1, len(text)//2 + 1):
        for i in range(len(text) - 2 * size + 1):
            pattern = text[i:i+size]
            next_pattern = text[i+size:i+2*size]

            if pattern == next_pattern:
                # Ensure it does NOT repeat more than twice
                third_start = i + 2 * size
                if third_start + size <= len(text) and text[third_start:third_start+size] == pattern:
                    continue  # skips if more than twice

                return True
    return False

def is_made_up_of_seqeuntial_pattern(text: str) -> bool:
    n = len(text)

    # try every possible pattern size (must divide length into exactly 2 parts)
    if n % 2 != 0:
        return None  # odd length can never be 2 repeats of equal-size blocks

    size = n // 2
    pattern = text[:size]

    return text == pattern + pattern

def is_invalid(val: str) -> bool:
    # Check if starts with 0 or has a sequential pattern that happens twice
    return is_made_up_of_seqeuntial_pattern(val)

def calculate_password(puzzle_input: List[str]) -> str:
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

    password = calculate_password(puzzle_input)

    # print(f"{password=}, {(password == 1227775554)=}")
    print(f"{password=}")

    pause = 1
