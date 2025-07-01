import random
from collections import Counter

students = ["Alice", "Bob", "Charlie", "Diana"]
days = 9

attended_day = []
for _ in range(days):
    present_count = random.randint(1, len(students))
    today = random.sample(students, present_count)
    attended_day.append(today)

attended_flat = [name for day in attended_day for name in day]

result = Counter(attended_flat)

for k in sorted(result):
    print(f"{k}: был(а) на {result[k]} занятиях")

top_students = [name for name in students if result.get(name, 0) == days]
if top_students:
    print("\nСамые ответственные:", ", ".join(top_students))
else:
    print("\nНет студентов, кто был на всех занятиях")
