# App for rotating pdf pages

import easygui as gui
from PyPDF2 import PdfFileWriter, PdfFileReader

# Display a file selection dialog for opening a PDF file.

path_to_file = gui.fileopenbox(
    title="Select a pdf file...",
    default="*.pdf"
)
# If the user cancels the dialog, then exit the program.

if path_to_file == None:
    exit()

# Let the user select one of 90, 180 or 270 degrees to rotate the PDF pages.

choices = ["90", "180", "270"]
rotation_degrees = gui.buttonbox(
    msg="Rotate pdf pages clockwise how many degrees?",
    choices=choices
)


rotation_degrees = int(rotation_degrees)  # Convert rotation degrees to int.

# Display a file selection dialog for saving the rotated PDF.
deffault_file_name=f"rotated{rotation_degrees}.pdf"
save_path = gui.filesavebox(
    title="Save file to...",
    default=deffault_file_name
)
# If the user tries to save a file with the same name as the input file:

while save_path == path_to_file:
    # Alert the user with a message box that this is not allowed.
    gui.msgbox(
        msg="The new file can't have the same name as the old file",
        title="Warning"
    )
    # Return to previous step.
    save_path = gui.filesavebox(
        title="Save file to...",
        default=deffault_file_name
    )
# If the user cancels the file save dialog, then exit the program.

if save_path == None:
    exit()

# Perform the page rotation:

# Open the selected PDF.

pdf_reader = PdfFileReader(path_to_file)
pdf_writer = PdfFileWriter()

# Rotate all of the pages.
for page in pdf_reader.pages:
    page.rotateClockwise(rotation_degrees)
    pdf_writer.addPage(page)

# Save the rotated PDF to the selected file.

with open(save_path, mode="wb") as output_file:
    pdf_writer.write(output_file)
    gui.msgbox(
        msg="Finished"
    )
