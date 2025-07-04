from typing import List, Dict
from collections import defaultdict

def read_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read().lower().replace('\n', ' ')



def clear_text(text: str) -> List[str]:
    new_text = ''
    for i in range(len(text)):
        char = text[i]
        if char == "-":
            if 0 < i < len(text) - 1:
                if text[i-1].isalpha() and text[i+1].isalpha():
                    new_text += char
        elif char.isalpha() or char.isspace():
            new_text += char
    return new_text.split()

def count_ngrams(words: List[str], n: int) -> Dict[str, int]:
    ngrams = defaultdict(int)
    for i in range(len(words) - n + 1):
        ngram = ' '.join(words[i:i + n])
        ngrams[ngram] += 1
    return dict(ngrams)

def main():
    n = int(input("Введите размер n-граммы: "))
    file = 'test2.txt'
    text = read_text(file)
    words = clear_text(text)
    ngrams = count_ngrams(words, n)
    print(list(ngrams.items())[:10])


if __name__ == '__main__':
    main()