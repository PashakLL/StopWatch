import tkinter as tk

root = tk.Tk()
root.title("Помодоро")
label = tk.Label(root, text="Нажмите", font=("Arial", 60))
label.pack()


seconds_in_minute = 1
work_minutes = 25
rest_minutes = 5


def start():
    go_down(work_minutes * seconds_in_minute, 'Работа')


def format_time(total_seconds):
    minute = total_seconds // 60
    sec = total_seconds % 60
    return f"{minute:02}:{sec:02}"


def go_down(timer, phase):
    line = format_time(timer)
    label.config(text=f"{line} {phase}")
    if timer > 0:
        root.after(1000, go_down, timer - 1, phase)
    else:
        if phase == 'Работа':
            phase = 'Отдых'
            root.after(
                1000, go_down, rest_minutes * seconds_in_minute - 1, phase
                )
        else:
            phase = 'Работа'
            root.after(
                1000, go_down, work_minutes * seconds_in_minute - 1, phase
                )


button = tk.Button(root, text="Старт", command=start)
button.pack()
root.mainloop()
