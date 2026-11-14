import time


#text = input("Сколько минут необходимо засечь? ")
work_seconds = 5
rest_seconds = 3
        
def format_time(total_seconds):
    minute = int(total_seconds // 60)
    sec = int(total_seconds % 60)
    return f"{minute:02}:{sec:02}"


def countdown(total_seconds):
    for step in range(1, total_seconds+1):
        time.sleep(1)
        tik = int(total_seconds - step)
        print(f"Осталось {format_time(tik)}")
    print("Время вышло")




print("Работа")
countdown(work_seconds)
print("Отдых")
countdown(rest_seconds)
# try:
#     timer = int(text)
#     if timer <= 0:
#         print("Число должно быть больше нуля")
#     else:
#         timer_sec = timer * 60
#         print(f"Это {timer_sec} секунд")
#         for step in range(1, timer_sec+1):
#             time.sleep(1)
#             tik = int(timer_sec - step)
#             print(f"Осталось {format_time(tik)}")
#         print("Время вышло")
# except ValueError:
#     print("засечь буквы невозможно")    
# except KeyboardInterrupt:
#     print("Остановлено")

