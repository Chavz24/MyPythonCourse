"""Challenge: Return of the Poet 18.10"""

import tkinter as tk
from OO_Generate_button import generate_button

window = tk.Tk()

window.columnconfigure(
    index=0,
    minsize=600,
    weight=1
)
window.rowconfigure(
    index=2,
    weight=1
)

frm_entries = tk.Frame(
    master=window
)
frm_entries.rowconfigure(
    index=6,
)
frm_entries.columnconfigure(
    index=1,
    weight=1,
)

lbl_intruction = tk.Label(
    master=frm_entries,
    text="Enter your favorites words separated by commas",
)
lbl_intruction.grid(
    row=0,
    column=1,
    pady=20
)
word_types = ["Nouns", "Verbs", "Adjectives", "Prepositions", "Adverbs"]

# This for loop generates all the entry boxes with their labels.
lbl_word_noun = tk.Label(
    master=frm_entries,
    text=f"{word_types[0]}:"
)
lbl_word_noun.grid(
    row=1,
    column=0,
    pady=5,
    sticky="e"
)
lbl_word_verb = tk.Label(
    master=frm_entries,
    text=f"{word_types[1]}:"
)
lbl_word_verb.grid(
    row=2,
    column=0,
    pady=5,
    sticky="e"
)
lbl_word_adj = tk.Label(
    master=frm_entries,
    text=f"{word_types[2]}:"
)
lbl_word_adj.grid(
    row=3,
    column=0,
    pady=5,
    sticky="e"
)
lbl_word_prep = tk.Label(
    master=frm_entries,
    text=f"{word_types[3]}:"
)
lbl_word_prep.grid(
    row=4,
    column=0,
    pady=5,
    sticky="e"
)
lbl_word_adv = tk.Label(
    master=frm_entries,
    text=f"{word_types[4]}:"
)
lbl_word_adv.grid(
    row=5,
    column=0,
    pady=5,
    sticky="e"
)
ent_word_noun = tk.Entry(
    master=frm_entries,
)
ent_word_noun.grid(
    row=1,
    column=1,
    sticky="ew"
)
ent_word_verb = tk.Entry(
    master=frm_entries,
)
ent_word_verb.grid(
    row=2,
    column=1,
    sticky="ew"
)
ent_word_adj = tk.Entry(
    master=frm_entries,
)
ent_word_adj.grid(
    row=3,
    column=1,
    sticky="ew"
)
ent_word_prep = tk.Entry(
    master=frm_entries,
)
ent_word_prep.grid(
    row=4,
    column=1,
    sticky="ew"
)
ent_word_adv = tk.Entry(
    master=frm_entries,
)
ent_word_adv.grid(
    row=5,
    column=1,
    sticky="ew"
)

btn_poem_generator = tk.Button(
    master=window,
    text="Generate",
    command=generate_button
)

frm_entries.grid(
    padx=5,
    sticky="nsew"
)
btn_poem_generator.grid(
    row=1,
    column=0,
    sticky="s",
    pady=20
)

# Frame for te result.

frm_poem = tk.Frame(
    master=window,
    relief=tk.SUNKEN,
    borderwidth=2
)
frm_poem.rowconfigure(
    index=1,

)
frm_poem.columnconfigure(
    index=0,
    weight=1,
)

lbl_poem = tk.Label(
    master=frm_poem,
    text="Please enter 3 nous, 3 verbs,3 adjectives"
         "\n3 prepositions and one adverb and then"
         "\npress the generate button to create a poem"

)

lbl_poem.grid(
    row=0,
    column=0,
    pady=30,
    sticky="ew",
)
btn_save_poem = tk.Button(
    master=frm_poem,
    text="Save to file",
    command=None  # TODO
)
btn_save_poem.grid(
    row=1,
    column=0,
    sticky="n",
    pady=5,
)
frm_poem.grid(
    row=2,
    column=0,
    padx=5,
    pady=5,
    sticky="new"
)
window.mainloop()
