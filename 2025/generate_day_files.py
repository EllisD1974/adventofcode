import os
import requests
from bs4 import BeautifulSoup

AOC_YEAR = 2025
SESSION_TOKEN = "53616c7465645f5f67f1bc310278602d7802215471edd5480ebb7350850e3029781e538a9e0f91a62f95eaf706ba646dc2db259c98c00aea60a91bc71b239373"

def get_next_day_number(file_path="last_day.txt"):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            number = int(f.read().strip()) + 1
    else:
        number = 1

    with open(file_path, "w") as f:
        f.write(str(number))

    return number

def fetch_page(url, use_auth=False):
    headers = {}
    if use_auth:
        headers["Cookie"] = f"session={SESSION_TOKEN}"

    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.text

def save_file(path, contents):
    with open(path, "w", encoding="utf-8") as f:
        f.write(contents)

def main():
    day = get_next_day_number()
    folder_name = f"day{day}"
    os.makedirs(folder_name, exist_ok=True)

    # Fetch prompt
    prompt_url = f"https://adventofcode.com/{AOC_YEAR}/day/{day}"
    prompt_html = fetch_page(prompt_url)

    # Strip HTML for cleaner prompt
    soup = BeautifulSoup(prompt_html, "html.parser")
    article = soup.find("article")
    prompt_text = article.text if article else prompt_html

    save_file(os.path.join(folder_name, "prompt.txt"), prompt_text)

    # Fetch puzzle input (requires session cookie)
    input_url = f"https://adventofcode.com/{AOC_YEAR}/day/{day}/input"
    puzzle_input = fetch_page(input_url, use_auth=True)
    save_file(os.path.join(folder_name, "puzzle_input.txt"), puzzle_input)

    # Create template Python files
    pt1_file = os.path.join(folder_name, f"day{day}_pt1.py")
    pt2_file = os.path.join(folder_name, f"day{day}_pt2.py")

    save_file(pt1_file, f"""# Day {day} - Part 1\n\ndef solve(data):\n    pass\n\nif __name__ == "__main__":\n    with open("puzzle_input.txt") as f:\n        data = f.read().strip().splitlines()\n    solve(data)\n""")

    save_file(pt2_file, f"""# Day {day} - Part 2\n\ndef solve(data):\n    pass\n\nif __name__ == "__main__":\n    with open("puzzle_input.txt") as f:\n        data = f.read().strip().splitlines()\n    solve(data)\n""")

    print(f"Created: {folder_name}")

if __name__ == "__main__":
    main()
