"""Challenge: Return of the Poet 18.10"""

import tkinter as tk

window = tk.Tk()

window.columnconfigure(
    index=0,
    minsize=600,
    weight=1
)
window.rowconfigure(
    index=0,
    minsize=600,
    weight=1
)

frm_entries = tk.Frame(
    master=window
)

lbl_intruction = tk.Label(
    master=frm_entries,
    text="Enter your favorites words separated by commas",
)
lbl_intruction.grid(
    row=0,
    column=1,
    sticky="n",
    padx=280,
    pady=20
)
word_types = ["Nouns", "Verbs", "Adjectives", "Prepositions", "Adverbs"]

# This for loop generates all the entry boxes with their labels.
for word in word_types:
    lbl_word = tk.Label(
        master=frm_entries,
        text=f"{word}:"
    )
    ent_word = tk.Entry(
        master=frm_entries
    )
    lbl_word.grid(
        row=word_types.index(word) + 1,
        column=0,
        pady=5,
        sticky="e"
    )
    ent_word.grid(
        row=word_types.index(word) + 1,
        column=1,
        pady=5,
        sticky="ew",
        padx=5
    )

btn_poem_generator=tk.Button(
    master=frm_entries,
    text="Generate",
    command=None  # TODO
)
btn_poem_generator.grid(
    row=6,
    column=1,
    sticky="n"
)
frm_entries.grid(
    sticky="nsew"
)

# Todo: poem frame and its widgets

window.mainloop()
