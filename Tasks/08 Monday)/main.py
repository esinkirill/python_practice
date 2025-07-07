from collections import defaultdict


def clear_text(text: str) -> str:
    return text.lower()


def analize_text(text: str) -> dict:
    letters = defaultdict(int)
    punctuation = defaultdict(int)
    spaces = defaultdict(int)

    for char in text:
        if char.isalpha():
            letters[char] += 1
        elif char.isspace():
            spaces[char] += 1
        else:
            punctuation[char] += 1

    return {'letters': letters, 'punctuation': punctuation, 'spaces': spaces}


def main():
    input_string = 'Hello, world! Привет, мир!'
    clean = clear_text(input_string)
    result = analize_text(clean)

    print("Букв:", sum(result['letters'].values()))
    print("Знаков препинания:", sum(result['punctuation'].values()))
    print("Пробелов:", sum(result['spaces'].values()))


if __name__ == '__main__':
    main()
