import tkinter as tk

# The .pack() Geometry manager

# window = tk.Tk()
#
# frm1 = tk.Frame(
#     master=window,
#     bg="red",
#     width=100,
#     height=100
# )
# frm1.pack(
#     fill=tk.BOTH,
#     side=tk.LEFT,
#     expand=True
# )
#
# frm2 = tk.Frame(
#     master=window,
#     width=50,
#     height=50,
#     bg="yellow"
# )
# frm2.pack(
#     fill=tk.BOTH,
#     side=tk.LEFT,
#     expand=True
# )
#
# frm3 = tk.Frame(
#     master=window,
#     width=25,
#     height=25,
#     bg="blue"
# )
# frm3.pack(
#     fill=tk.BOTH,
#     side=tk.LEFT,
#     expand=True
# )
#
# window.mainloop()


# window = tk.Tk()
#
# frm = tk.Frame(
#     master=window,
#     width=150,
#     height=150
# )
# frm.pack()
#
# lbl1 = tk.Label(
#     master=frm,
#     text="I'm at (0,0)",
#     bg="purple"
# )
# lbl1.place(
#     x=0,
#     y=0
# )
# lbl2 = tk.Label(
#     master=frm,
#     text="I'm at (75,75)",
#     bg="lightblue"
# )
# lbl2.place(
#     x=75,
#     y=130
# )
# window.mainloop()


# The .grid() Geometry manager

# window = tk.Tk()
#
# for i in range(3):
#     window.rowconfigure(i, weight=1, minsize=1)
#     window.columnconfigure(i, weight=1, minsize=50)
#
#     for j in range(3):
#         frm = tk.Frame(
#             master=window,
#             relief=tk.RIDGE,
#             borderwidth=1
#         )
#         frm.grid(
#             row=i,
#             column=j,
#             padx=5,
#             pady=5
#         )
#         lbl = tk.Label(
#             master=frm,
#             text=f"This is row {i + 1}\ncolumn {j + 1}."
#         )
#         lbl.pack(
#             padx=2,
#             pady=2
#         )
#
# window.mainloop()

window = tk.Tk()

window.rowconfigure(0, minsize=50)
window.columnconfigure([0, 1, 2, 3], minsize=50)

lbl1 = tk.Label(
    text="1",
    bg="aqua",
    fg="red"
)
lbl1.grid(
    row=0,
    column=0,

)

lbl2 = tk.Label(
    text="2",
    bg="aqua",
    fg="red"
)
lbl2.grid(
    row=0,
    column=1,
    sticky="ns",
)

lbl3 = tk.Label(
    text="3",
    bg="aqua",
    fg="red"
)
lbl3.grid(
    row=0,
    column=2,
    sticky="ew",
)

lbl4 = tk.Label(
    text="4",
    bg="aqua",
    fg="red"
)
lbl4.grid(
    row=0,
    column=3,
    sticky="nsew",
)

window.mainloop()
