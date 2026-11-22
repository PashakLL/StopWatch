import tkinter as tk

root = tk.Tk()
root.title("Помодоро")
label = tk.Label(root, text="10", font=("Arial", 60))
label.pack()


def go_down(timer):
    label.config(text=timer)
    if timer > 0:
        root.after(1000, go_down, timer - 1)
    else:
        label.config(text='Готово')


go_down(10)
root.mainloop()
