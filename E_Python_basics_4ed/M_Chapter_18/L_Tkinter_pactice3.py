"""Review Exercises 18.7"""

# Write a program that displays a single button with the default
# background color and black text that reads"Click me".
# When the user clicks on the button, the button background
# should change to a color randomly selected from a list.

import tkinter as tk
from random import choice, randint


# color_choices = [
#     "red", "orange", "yellow",
#     "blue", "green", "indigo",
#     "violet"
# ]
#
#
# def color_change():
#     color = choice(color_choices)
#     btn_click["bg"] = f"{color}"
#
#
# window = tk.Tk()
#
# btn_click = tk.Button(
#     master=window,
#     text="Click me",
#     bg=None,
#     command=color_change
# )
#
# btn_click.grid(
#     padx=10,
#     pady=10
# )
#
# window.mainloop()

# Write a program that simulates rolling a six-sided die. There
# should be one button with the text "Roll". When the user clicks
# the button, a random integer from 1 to 6 should be displayed.

def random_number():
    number = randint(1, 6)
    lbl_dice_number["text"] = f"{number}"


window = tk.Tk()

btn_roll = tk.Button(
    master=window,
    text="Roll",
    command=random_number
)

lbl_dice_number = tk.Label(
    master=window,
    text=None
)

btn_roll.pack()
lbl_dice_number.pack()

window.mainloop()
