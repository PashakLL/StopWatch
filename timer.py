import time



templates = {
    '1': (5, 2),
    '2': (7, 3)
}

cycles = 2

def format_time(total_seconds):
    minute = int(total_seconds // 60)
    sec = int(total_seconds % 60)
    return f"{minute:02}:{sec:02}"


def countdown(total_seconds):
    for step in range(0, total_seconds):
        tik = int(total_seconds - step)
        print(f"Осталось {format_time(tik)}")
        time.sleep(1)
    print("Время вышло")

def timer_pomodoro(work_seconds, rest_seconds):
    for number in range(1, cycles + 1):
        print("Подход", number, "из", cycles)
        print("Работа")
        countdown(work_seconds)
        print("Отдых")
        countdown(rest_seconds)

choice = input("Введите название шаблона? ")

try:
    if choice in templates:
        work_seconds, rest_seconds = templates[choice]
        timer_pomodoro(work_seconds, rest_seconds)
    elif choice == '0':
        work_seconds, rest_seconds = int(input("Введите сколько времени будете работать ")), int(input("Введите сколько времени будете отдыхать "))
        if work_seconds <= 0 or rest_seconds <= 0:
            print("Время должно быть больше 0")
        else:
            timer_pomodoro(work_seconds, rest_seconds)
    else:
        print("Такого шаблона нет")
except ValueError:
    print("засечь буквы невозможно")
except KeyboardInterrupt:
    print("Остановлено")