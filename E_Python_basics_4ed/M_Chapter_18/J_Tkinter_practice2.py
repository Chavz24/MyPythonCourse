"""Review Exrcises 18.6"""

# Try and recreate the window using the techniques you have learned thus far.
# You may use any geometry manager you like. (see page 607)



import tkinter as tk
from string import capwords

window = tk.Tk()

window.title("Address Entry Form")

frm_form = tk.Frame(
    width=400,
    height=200,
    relief=tk.SUNKEN,
    borderwidth=5
)
frm_form.pack()

form_row = [
    "first name", "last name", "address line 1",
    "address line 2", "city", "state / province",
    "postal code", "country"
]

for row in form_row:
    for j in range(1):
        lbl_row = tk.Label(
            master=frm_form,
            text=f"{capwords(row)}:"
        )
        lbl_row.grid(
            row=form_row.index(row),
            column=0,
            sticky="e"
        )
        ent_box = tk.Entry(
            master=frm_form,
            width=50
        )
        ent_box.grid(
            row=form_row.index(row),
            column=1,
        )

btn_summit = tk.Button(
    text="Summit",
    width=10
)

btn_clear = tk.Button(
    text="Clear",
    width=10
)

btn_summit.pack(
    side=tk.RIGHT,
    padx=10,
    pady=10
)

btn_clear.pack(
    side=tk.RIGHT,
    padx=10,
    pady=10
)

window.mainloop()
