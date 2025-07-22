import tkinter as tk
from time import strftime

def time():
    current_time = strftime('%H:%M:%S \n %D')
    label.config(text=current_time)
    label.after(1000, time)

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=('calibri', 50, 'bold'), background='yellow', foreground='black')
label.pack(anchor='center')

time()

root.mainloop()
