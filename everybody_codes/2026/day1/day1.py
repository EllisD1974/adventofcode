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






if __name__ == "__main__":
    notes = parse_notes(Path("./notes.txt"))

    notes = [3,11,12,16,24,25]

    total_remaining = 0
    for p in notes:
        n = get_max_n_for_full_matrix(p)
        rem = (n * n) - p
        total_remaining += rem

    print(total_remaining)
