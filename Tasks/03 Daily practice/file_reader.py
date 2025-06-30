# 1) Открываем для чтения и сохраняем оригинал
with open('test.txt', 'r', encoding='utf-8') as f:
    original = f.read()

print("Оригинал:")
print(original)


# 2) Открываем в режиме 'w' — файл обрежется и запишем новое
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write("hello\n")

print("\nПосле записи 'hello':")
with open('test.txt', 'r', encoding='utf-8') as f:
    print(f.read())


# 3) Открываем в режиме 'a' (append) и дописываем оригинал
with open('test.txt', 'w+', encoding='utf-8') as f:
    f.write(original)

# 4) Снова читаем весь файл и выводим
print("\nИтоговый файл:")
with open('test.txt', 'r', encoding='utf-8') as f:
    print(f.read())
