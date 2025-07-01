import json
import os
import datetime

FILENAME = "time_log.json"

def load_sessions():
    """Загружает список всех сессий из файла."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


def save_sessions(sessions):
    """Сохраняет список сессий в файл."""
    with open(FILENAME, "w") as file:
        json.dump(sessions, file, indent=2)


def format_time(seconds):
    """Форматирует секунды в строку чч:мм:cc."""
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"


def sum_sessions(sessions, days=None):
    """Считает сумму времени всех сессий,
    если days указаны — только за последние N дней."""
    now = datetime.datetime.now()
    total = 0
    for session in sessions:
        session_time = float(session["seconds"])
        session_date = datetime.datetime.strptime(session["date"], "%Y-%m-%d %H:%M:%S")
        if days is None or (now - session_date).days < days:
            total += session_time
    return total


def main():
    print("Таймер Python — отслеживание времени учёбы!\n")

    sessions = load_sessions()

    input("Нажмите Enter для начала работы...")
    start = datetime.datetime.now()

    input("Нажмите Enter, когда закончите: ")
    end = datetime.datetime.now()
    delta = end - start

    seconds = delta.total_seconds()
    print(f"\nВаша сессия: {format_time(seconds)}")

    sessions.append({
        "date": start.strftime("%Y-%m-%d %H:%M:%S"),
        "seconds": seconds
    })
    save_sessions(sessions)

    total = sum_sessions(sessions)
    last_2weeks = sum_sessions(sessions, days=14)
    print(f"\nВсего времени за всё время: {round(total / 3600, 2)} часов")
    print(f"В том числе за последние 2 недели: {round(last_2weeks / 3600, 2)} часов")
    input("\nНажмите Enter для закрытия окна...")

if __name__ == "__main__":
    main()
