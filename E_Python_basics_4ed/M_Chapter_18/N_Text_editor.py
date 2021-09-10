"""Example App: Text Editor 18.9"""

# An app that lets you create a text and save it.

import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox


def open_file():
    """This function opens the file"""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    elif not filepath.endswith(".txt"):
        return messagebox.showerror("Error", "Can only open files with .txt extension.")
    txt_edit.delete("1.0", tk.END)

    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)

    window.title(f"Chavez24 Text editor {filepath}")


def save_file():
    """This function saves the edited document"""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        initialfile="Modified_text"
    )

    if not filepath:
        return
    elif not filepath.endswith(".txt"):
        return messagebox.showerror("Error", "Can only save files with .txt extension.")
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)

    window.title(f"Chavez24 Text editor - {filepath}")


window = tk.Tk()

window.title("Chavez24 Text editor")

window.rowconfigure(
    index=0,
    minsize=600,
    weight=1
)
window.columnconfigure(
    index=1,
    minsize=600,
    weight=1
)
# Displays buttons on the left side.
frm_buttons = tk.Frame(
    master=window
)
frm_buttons.grid(
    row=0,
    column=0,
    sticky="ns"
)
# The open file button.
btn_open = tk.Button(
    master=frm_buttons,
    text="Open",
    command=open_file
)
btn_open.grid(
    row=0,
    column=0,
    sticky="ew",
    padx=5,
    pady=10
)
# Save file button
btn_save = tk.Button(
    master=frm_buttons,
    text="Save as",
    command=save_file
)

btn_save.grid(
    row=1,
    column=0,
    sticky="ew",
    padx=5,
    pady=10
)

# Text editor box.

# Setting up the scroll bars (Vertical and Horizontal).
scr_horizontal = tk.Scrollbar(
    master=window,
    orient=tk.HORIZONTAL
)
scr_horizontal.grid(
    row=1,
    column=1,
    sticky="ew"
)
scr_vertical = tk.Scrollbar(
    master=window,
)
scr_vertical.grid(
    row=0,
    column=2,
    sticky="ns"
)
# Setting up the text editor.
txt_edit = tk.Text(
    master=window,
    yscrollcommand=scr_vertical.set,
    xscrollcommand=scr_horizontal.set
)
txt_edit.grid(
    row=0,
    column=1,
    sticky="nsew"
)
# Binding the scroll bar to the text editor.
scr_horizontal.configure(
    command=txt_edit.xview
)
scr_vertical.configure(
    command=txt_edit.yview
)
window.mainloop()
