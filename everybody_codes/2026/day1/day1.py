"""
Everybody codes - 2026 - DAY 1
https://everybody.codes/event/2026/quests/1
"""

from math import sqrt, ceil
from pathlib import Path

def parse_notes(notes_path: Path) -> list[int]:
    with open(notes_path, "r") as notes_file:
        notes = [int(i) for i in notes_file.read().strip().split(",")]
    return notes

def get_max_n_for_full_matrix(p: int) -> int:
    return ceil(sqrt(p))

def get_max_n_for_perimeter_matrix(p: int) -> int:
    max_n = ceil((p + 4) / 4)
    if max_n < 3:
        return 3
    return max_n

def get_perimeter_spaces(n: int) -> int:
    return (4 * n) - 4

def get_max_n_for_full_excluding_center_matrix(p: int) -> int:
    max_n = ceil(sqrt(p + 1))
    if max_n < 3:
        return 3

    if max_n % 2 == 0:
        return max_n + 1

    return max_n


if __name__ == "__main__":
    ## PART 1
    notes = parse_notes(Path("./notes.txt"))

    # notes = [3,11,12,16,24,25]

    total_remaining = 0
    for p in notes:
        n = get_max_n_for_full_matrix(p)
        rem = (n * n) - p
        total_remaining += rem

    print(total_remaining)

    ## PART 2
    notes = parse_notes(Path("./notes2.txt"))

    # notes = [3, 11, 12, 16, 24, 25]

    total_remaining = 0
    for p in notes:
        n = get_max_n_for_perimeter_matrix(p)
        rem = get_perimeter_spaces(n) - p
        total_remaining += rem

    print(total_remaining)

    ## PART 3
    notes = parse_notes(Path("./notes3.txt"))

    # notes = [3, 11, 12, 16, 24, 25]

    total_remaining = 0
    for p in notes:
        n = get_max_n_for_full_excluding_center_matrix(p)
        rem = (n * n) - 1 - p
        total_remaining += rem

        # print(f"{p=}, {n=}, {rem=}")

    print(total_remaining)
