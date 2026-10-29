"""
Everybody codes - 2026 - DAY 1
https://everybody.codes/event/2026/quests/1
"""

from math import sqrt, ceil
from pathlib import Path
from re import split as re_split

def parse_notes(notes_path: Path) -> list[int]:
    notes = []
    with open(notes_path, "r") as notes_file:
        for line in notes_file:
            notes.append([i for i in line.strip().split(" ")])
    return notes

def order_note_group(group: list[str]) -> list[int]:
    # Get rules, i.e. list of tuples for allowed orders
    # and get all unique numbers
    allowed_rule_groups = []
    unique_nums = set()
    for g in group:
        sep = [int(i) for i in re_split(r"[<>]", g)]
        if "<" in g:
            allowed_rule_groups.append((sep[1], sep[0]))
            unique_nums.add(sep[1])
            unique_nums.add(sep[0])

        elif ">" in g:
            allowed_rule_groups.append((sep[0], sep[1]))
            unique_nums.add(sep[0])
            unique_nums.add(sep[1])

    graph = {num: [] for num in unique_nums}
    counts = {num: 0 for num in unique_nums}

    for b, a in allowed_rule_groups:
        graph[b].append(a)
        counts[a] += 1

    x = [num for num in unique_nums if counts[num] == 0]
    ordered_group = []

    while x:
        current_num = x.pop(0)
        ordered_group.append(current_num)

        for next_num in graph[current_num]:
            counts[next_num] -= 1

            if counts[next_num] == 0:
                x.append(next_num)

    return ordered_group


if __name__ == "__main__":
    ## PART 1
    notes = parse_notes(Path("./notes1.txt"))

    # notes = parse_notes(Path("./test_notes1.txt"))

    totals = []
    total = 0
    for n in notes:
        print(n)


        t = int("".join(map(str, order_note_group(n))))

        totals.append(t)
        total += t

    print(f"{total=}")

    ## PART 2
    notes = parse_notes(Path("./notes2.txt"))

    # notes = parse_notes(Path("./test_notes2.txt"))

    totals = []
    total = 0
    for n in notes:
        print(n)

        t = int("".join(map(str, order_note_group(n))))

        totals.append(t)
        total += t

    print(f"{total=}")

    ## PART 3
    notes = parse_notes(Path("./notes3.txt"))

    # notes = parse_notes(Path("./test_notes3.txt"))

    totals = []
    total = 0
    for n in notes:
        print(n)

        t = int("".join(map(str, order_note_group(n))))

        totals.append(t)
        total += t

    print(f"{total=}")
