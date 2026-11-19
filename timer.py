import time


templates = {
    # Для быстрых задач, разминки перед работой и когда сложно сосредоточиться
    'Мини': (10, 3, 4),
    # Для лёгкого старта, коротких задач и дней с низкой концентрацией
    'Короткий': (15, 5, 4),
    # Для учёбы, небольших задач и борьбы с прокрастинацией
    'Классический': (25, 5, 4),
    # Для программирования, чтения, написания текстов и учёбы
    'Удлиненный': (50, 10, 2),
    # Для сложных проектов, разработки, творчества и задач, требующих погружения
    'Глубокая работа': (90, 20, 1)
}

seconds_in_minute = 60


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

def timer_pomodoro(work, rest, cycles):
    for number in range(1, cycles + 1):
        print("Подход", number, "из", cycles)
        print("Работа")
        countdown(work)
        print("Отдых")
        countdown(rest)

choice = input("Введите название шаблона? ")
cycles = 2
try:
    if choice in templates:
        work, rest, cycles = templates[choice]
        timer_pomodoro(
            work * seconds_in_minute, rest * seconds_in_minute, cycles
            )
    elif choice == '0':
        work = int(input("Введите сколько минут будете работать "))
        rest = int(input("Введите сколько минут будете отдыхать "))
        cycles = int(input("Введите сколько кругов будет "))
        if work <= 0 or rest <= 0 or cycles <= 0:
            print("Все числа должны быть больше 0")
        else:
            timer_pomodoro(
                work * seconds_in_minute, rest * seconds_in_minute, cycles
                )
    else:
        print("Такого шаблона нет")
except ValueError:
    print("засечь буквы невозможно")
except KeyboardInterrupt:
    print("Остановлено")