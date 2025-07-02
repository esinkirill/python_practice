with open('test.txt', encoding='utf-8') as my_file:
    text = my_file.read()

print(text)

def is_vowel(letter):
    return letter.lower() in "аеёиоуыэюяaeiou"


vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha() and char not in "ьъ":
        if is_vowel(char):
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Гласных: {vowel_count}")
print(f"Согласных: {consonant_count}")
