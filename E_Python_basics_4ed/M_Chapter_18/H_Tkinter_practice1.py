"""Review Exercises 18.5"""

import tkinter as tk

# Write a program that displays a Button widget that is 50 text units
# wide and 25 text units tall and has a white background with blue
# text that reads "Click here".

# window = tk.Tk()
#
# btn = tk.Button(
#     master=window,
#     width=50,
#     height=25,
#     bg="white",
#     fg="blue",
#     text="Click Here"
# )
#
# btn.pack()
#
# window.mainloop()

# Write a program that displays an Entry widget that is 40 text units
# wide and has a white background and black text. Use the .insert()
# method to display text in it that reads "What is your name?".

window = tk.Tk()

ent = tk.Entry(
    width=40
)
ent.insert(0, "What's your name?")
ent.pack()
window.mainloop()
