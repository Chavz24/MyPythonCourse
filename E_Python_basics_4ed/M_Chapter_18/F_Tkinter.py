import tkinter as tk

window = tk.Tk()

greet = tk.Label(text="Hello, World from tkinter.")
hype = tk.Label(text="Guis are awesome")
python = tk.Label(text="Python rocks")
start = tk.Label(text="Engage")
greet.pack()
hype.pack()
python.pack()
start.pack()

window.mainloop()
