from collections import defaultdict
from typing import List, Dict

def read_file(path: str) -> str:
    """Считывает файл и приводит текст к нижнему регистру."""
    with open(path, 'r', encoding='utf-8') as file:
        return file.read().lower().replace('\n', ' ')

def clear_text(text: str) -> List[str]:
    """
    Удаляет все знаки препинания, оставляет буквы, пробелы и дефисы внутри слов.
    Возвращает список слов.
    """
    new_text = ""
    for i in range(len(text)):
        char = text[i]
        if char == "-":
            if 0 < i < len(text) - 1:
                if text[i-1].isalpha() and text[i+1].isalpha():
                    new_text += char
        elif char.isalpha() or char.isspace():
            new_text += char
    return new_text.split()

def count_words(words: List[str], min_length: int) -> Dict[str, int]:
    """
    Считает частоту встречаемости слов длиной больше min_length.
    Возвращает словарь: {слово: количество}
    """
    counts = defaultdict(int)
    for word in words:
        if len(word) > min_length:
            counts[word] += 1
    return dict(counts)

def print_results(title: str, results: Dict[str, int], top: int = None) -> None:
    """Печатает результаты, отсортированные по убыванию частоты. Можно ограничить top."""
    sorted_words = sorted(results.items(), key=lambda x: x[1], reverse=True)
    if top:
        sorted_words = sorted_words[:top]
    print(f"\n{title}")
    for word, count in sorted_words:
        print(f"{word}: {count}")

def main():
    # 1. Считываем файл
    text = read_file('test.txt')

    # 2. Очищаем текст, получаем список слов
    words = clear_text(text)

    # 3. Считаем слова длиннее N (N задаёт пользователь)
    min_length = int(input("Введите минимальную длину слова: "))
    word_counts = count_words(words, min_length)

    # 4. Выводим все результаты
    print_results(f"Частота слов длиннее {min_length} букв", word_counts)
    print_results(f"Топ-10 самых частых длинных слов", word_counts, top=10)

if __name__ == '__main__':
    main()