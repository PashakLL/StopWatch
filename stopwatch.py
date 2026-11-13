import time

 
def format_time(total_seconds):
    minute = int(total_seconds // 60)
    sec = int(total_seconds % 60)
    return f"{minute:02}:{sec:02}"

try:
    begin = time.time()
    while True:
        time.sleep(1)
        tik = int(time.time() - begin)
        print(f"Прошло {format_time(tik)}")
except KeyboardInterrupt:
     print("Остановлено")

end = time.time() - begin
print(f"Прошло {format_time(end)}")
