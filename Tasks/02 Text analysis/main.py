from docx import Document
import sys
import os

punctuation = '- ! " # $ % & \' ( ) * + , . / : ; < = > ? @ [ \\ ] ^ _ ` { | } ~ « » —'
punctuation = punctuation.split(" ")

# file_name = input("Enter path for .docx file: ")
file_name = "C:\\Users\\Kirill\\PycharmProjects\\gpt\\Tasks\\02 Text analysis\\text.docx"
if not os.path.exists(file_name):
    print("File not found")
    sys.exit()

text_input = " ".join(p.text for p in Document(file_name).paragraphs).lower()

print("\nОбщее количество слов: ",len(text_input.split()))

def my_isalpha(s):
    alphabet = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    s = s.lower()
    if not s:
        return False
    for _char1 in s:
        if _char1 not in alphabet:
            return False
    return True

clean_text = ""
for i in range(len(text_input)):
    char = text_input[i]

    if char == "-":
        if 0 < i < len(text_input) - 1:
            if my_isalpha(text_input[i - 1]) and my_isalpha(text_input[i + 1]):
                clean_text += "-"
    elif char not in punctuation:
        clean_text += char

words = clean_text.split()

stop_words = [
    "а", "но", "и", "или", "да", "что", "в", "на", "с", "из", "по", "к", "за",
    "же", "не", "ну", "то", "бы", "ли", "этот", "эта", "это", "тот", "та", "те", "что-то", "из-за"
]

filtered_words = [word for word in words if word not in stop_words]

unique_words = []
for word in filtered_words:
    if word not in unique_words:
        unique_words.append(word)

print("\nКоличество уникальных слов: ", len(unique_words))

shortest = None
longest = None

for word in unique_words:
    if shortest is None or len(word) < len(shortest) or (len(word) == len(shortest) and word < shortest):
        shortest = word
    if longest is None or len(word) > len(longest) or (len(word) == len(longest) and word < longest):
        longest = word

print(f"\nСамое короткое слово: {shortest}")
print(f"\nСамое длинное слово: {longest}")

word_counts = {}

for word in filtered_words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

top_5 = sorted_words[:5]

print("\nТоп-5 самых частых слов:")
for word, count in top_5:
    print(f"{word}: {count}")



