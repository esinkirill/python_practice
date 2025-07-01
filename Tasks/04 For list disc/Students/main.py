import random

students = ["Alice", "Bob", "Charlie", "Diana"]
days = 9

attended_day = []

for day in range(days):
    dayN = []
    _students = students.copy()
    for i in range(random.randint(1, len(students))):
        vote = random.choice(_students)
        if vote in dayN:
            _students.pop(_students.index(vote))
            vote = random.choice(_students)
            dayN.append(vote)
        else:
            dayN.append(vote)
    attended_day.append(dayN)

attended_day_full = []

for day_list in attended_day:
    for student in day_list:
        attended_day_full.append(student)

result = {}

for name in attended_day_full:
    result[name] = result.get(name, 0) + 1

for k, v in result.items():
    if v <= 2 and v % 2 == 0:
        print(f"{k} прогульщик был(а) всего {v} раза")
    elif v <= 2 and v % 2 != 0:
        print(f"{k} прогульщик был(а) всего {v} раз")
    else:
        print(f"{k} был(а) на {v} занятиях")

total_days = len(attended_day)
top_students = [name for name, count in result.items() if count == total_days]
if top_students:
    print("\nСамые ответственные:", ", ".join(top_students))
else:
    print("\nНет студентов, кто был на всех занятиях")
