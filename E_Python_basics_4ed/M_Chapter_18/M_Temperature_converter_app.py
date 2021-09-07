"""Example App: Temperature Converter 18.8"""

# A desktop app that converts degrees Fahrenheit to degrees Celsius.

import tkinter as tk


def temp_converter():
    """This function takes degrees Fahrenheit and convert them to Celsius"""
    try:
        degrees_fah = float(ent_temp.get())
        celsius = ((degrees_fah - 32) * 5) / 9
        lbl_result["text"] = f"{celsius:.2f} \N{DEGREE CELSIUS}"
        lbl_error["text"] = ""
    except ValueError:
        lbl_error["text"] = "You must enter a number\nExample:0.5 or 12 or 50.6."


window = tk.Tk()
window.title("Temperature Converter")

frm_convert = tk.Frame(
    master=window
)
frm_convert.grid(
    padx=5
)

ent_temp = tk.Entry(
    master=frm_convert,
    width=10
)

ent_temp.grid(
    row=0,
    column=0,
    sticky="e"
)

lbl_fahrenheit = tk.Label(
    master=frm_convert,
    text="\N{DEGREE FAHRENHEIT}"
)
lbl_fahrenheit.grid(
    row=0,
    column=1,
    sticky="w"
)

btn_converter = tk.Button(
    master=frm_convert,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=temp_converter,
)
btn_converter.grid(
    row=0,
    column=2,
    padx=5
)

lbl_result = tk.Label(
    master=frm_convert,
    text="\N{DEGREE CELSIUS}",
    width=10
)

lbl_result.grid(
    row=0,
    column=4,
    padx=5
)

lbl_error = tk.Label(
    text=""
)
lbl_error.grid(
    row=1
)
window.mainloop()
