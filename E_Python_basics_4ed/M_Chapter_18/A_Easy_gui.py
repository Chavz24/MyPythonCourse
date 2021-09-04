import easygui as gui


# nombre=gui.msgbox(msg="Miguel",title="You name")
#
# if nombre==None:
#     message=gui.msgbox(msg="No introduciste tu nombre",title="Advertencia")
#     exit()

# buttonbox

choices = ("The witcher 3", "Manga", "Anime")
# hobby = gui.buttonbox(
#     msg="Cual es tu hobbit favorito?",
#     title="Pick a hobby",
#     choices=list(choices)
# )


# Indexbox

# hobby = gui.indexbox(
#     msg="Cual es tu hobbit favorito?",
#     title="Pick a hobby",
#     choices=list(choices)
# )
# if not hobby==None:
#     print(choices[hobby])

# enterbox

# text=gui.enterbox(msg="What is your favorite hobby?",
#                   title="Pick a favorite hobby",
#                   default="Enter Hobby here",
#                   image="Captura.PNG")
# print(text)

# fileopenbox

# path_to_file=gui.fileopenbox(
#     msg="select a file",
#     title="Select a file",
#     default=r"C:\Users")
# print(path_to_file)

# diropenbox

# path_to_dir = gui.diropenbox(
#     msg="Open Dir",
#     title="Select a dir",
# )
# print(path_to_dir)

# filesavebox

# save_path=gui.filesavebox(
#     msg="Save dir",
#     title="Select a dir"
# )
# print(save_path)

msg = ""

while msg == "":
    msg = gui.msgbox(msg="seguro que desea salir?")
    print(msg)
