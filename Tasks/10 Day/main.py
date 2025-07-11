from typing import List

def multi_input(prompt="Введите числа (Enter — закончить):"):
    print(prompt)
    lines = []
    while True:
        line = input()
        if not line.strip():
            break
        lines.append(line)
    return '\n'.join(lines)

def clean_and_extract_numbers(text: str) -> list[float]:
    allowed = set('0123456789.,')
    cleaned = ''.join(ch if ch in allowed else ' ' for ch in text)
    cleaned = cleaned.replace(',', '.')
    numbers = []
    for token in cleaned.split():
        try:
            numbers.append(float(token))
        except ValueError:
            pass
    return numbers

def math_with_num(numbers: List[float]) -> None:
    max_num = max(numbers)
    min_num = min(numbers)
    mean_num = sum(numbers) / len(numbers)
    print("-" * 30)
    print(f"Ваши числа: {' '.join(map(str, numbers))}")
    print(f"Максимум: {max_num}")
    print(f"Минимум: {min_num}")
    print(f"Среднее арифметическое: {mean_num:.2f}")
    print("-" * 30)

def main() -> None:

    text = multi_input()
    numbers = clean_and_extract_numbers(text)
    math_with_num(numbers)

if __name__ == '__main__':
    main()