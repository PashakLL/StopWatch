import tkinter as tk

root = tk.Tk()
root.title("Помодоро")
label = tk.Label(root, text="10", font=("Arial", 60))
label.pack()


def format_time(total_seconds):
    minute = total_seconds // 60
    sec = total_seconds % 60
    return f"{minute:02}:{sec:02}"


def go_down(timer):
    line = format_time(timer)
    label.config(text=line)
    if timer > 0:
        root.after(1000, go_down, timer - 1)
    else:
        label.config(text='Готово')


go_down(10)
root.mainloop()
