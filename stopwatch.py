import time





input("Нажмите enter")
begin = time.time()
#input("Нажмите enter")

try:
    while True:
        time.sleep(1)
        tik = int(time.time() - begin)
        print(tik)
except KeyboardInterrupt:
    print("Остановлено")
 

end = time.time()
period = round(end - begin,2)
minute = int(period // 60)
sec = int(period % 60)

print(f"Прошло {minute} минут {sec} секунд")