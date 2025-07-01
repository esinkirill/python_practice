import json
import os
import datetime

FILENAME = "time_log.json"

def load_sessions():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_sessions(sessions):
    with open(FILENAME, "w") as file:
        json.dump(sessions, file, indent=2)

def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

def sum_sessions(sessions, days=None):
    now = datetime.datetime.now()
    total = 0
    for session in sessions:
        session_time = float(session["seconds"])
        session_date = datetime.datetime.strptime(session["date"], "%Y-%m-%d %H:%M:%S")
        if days is None or (now - session_date).days < days:
            total += session_time
    return total

def main():
    print("Таймер Python — отслеживание времени учёбы!")
    print("Во время сессии можно ставить паузу: напиши 'p' и нажми Enter.")
    print("Чтобы закончить, просто нажми Enter (без буквы).")

    sessions = load_sessions()
    input("Нажмите Enter для начала работы...")

    total_active = 0
    session_start = datetime.datetime.now()

    while True:
        pause = input("\nВведи 'p' и Enter для паузы, или просто Enter для завершения: ")
        if pause.lower() == "p":
            pause_start = datetime.datetime.now()
            input("Пауза. Нажмите Enter для продолжения...")
            pause_end = datetime.datetime.now()
            # Накопить только активное время!
            total_active += (pause_start - session_start).total_seconds()
            session_start = pause_end
        else:
            # Завершаем, учитываем финальный отрезок
            total_active += (datetime.datetime.now() - session_start).total_seconds()
            break

    print(f"\nВаша сессия: {format_time(total_active)}")

    # Сохраняем новую сессию
    sessions.append({
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "seconds": total_active
    })
    save_sessions(sessions)

    total = sum_sessions(sessions)
    last_2weeks = sum_sessions(sessions, days=14)
    print(f"\nВсего времени за всё время: {round(total / 3600, 2)} часов")
    print(f"В том числе за последние 2 недели: {round(last_2weeks / 3600, 2)} часов")

    input("\nНажмите Enter для закрытия окна...")

if __name__ == "__main__":
    main()
