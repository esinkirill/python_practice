from collections import defaultdict
from dataclasses import dataclass

@dataclass
class CharCounts:
    letters: dict
    punctuation: dict

def read_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().lower().replace(" ", "").replace("\n", "")

def count_characters(text):
    letters = defaultdict(int)
    punctuation = defaultdict(int)

    for char in text:
        if char.isalpha():
            letters[char] += 1
        else:
            punctuation[char] += 1

    return CharCounts(dict(letters), dict(punctuation))

def print_sorted_frequency(title, freq_dict, top=None):
    sorted_items = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    if top:
        sorted_items = sorted_items[:top]

    print(f"\n{title}:")
    for char, count in sorted_items:
        print(f"{char}: {count}")

def main():
    path = "test.txt"
    text = read_text(path)

    if not text:
        return

    result = count_characters(text)

    print_sorted_frequency("Буквы", result.letters)
    print_sorted_frequency("Знаки препинания", result.punctuation)
    print_sorted_frequency("Топ-10 символов", result.letters, top=10)

if __name__ == "__main__":
    main()
