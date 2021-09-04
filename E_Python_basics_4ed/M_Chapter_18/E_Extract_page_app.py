""" Challenge: PDF Page Extraction Application 18.3"""

# This is a pdf page extracting app.

import easygui as gui
from PyPDF2 import PdfFileWriter, PdfFileReader
from os.path import basename


def page_validator(page):
    """Converts the page number to an integer."""
    while True:
        try:
            page = int(page)
            if page < 1:
                # Warn the user that the entry is invalid .
                gui.msgbox(
                    msg="You must enter a number greater than 0"
                )
                page = gui.enterbox(
                    msg="Introduce the start page to extract",
                )
                continue
            else:
                break
        except (TypeError, ValueError):
            # Warn the user that the entry is invalid .
            gui.msgbox(
                msg="You must enter a number greater than 0"
            )
            # Return to previous step.
            page = gui.enterbox(
                msg="Introduce the start page to extract",
            )
            continue
    return page


# Ask the user to select a PDF file to open.

path_to_pdf = gui.fileopenbox(
    title="Select a file...",
    default="*.pdf"
)

# If no PDF file is chosen, exit the program.

if path_to_pdf is None:
    exit()
# Ask for a starting page number.

start_page = gui.enterbox(
    msg="Introduce the start page to extract",
)

#  If the user does not enter a starting page number, exit the program.

if start_page == "" or start_page is None:
    exit()

# If the user enters an invalid page number:

start_page = page_validator(start_page)

#  Ask for an ending page number.

end_page = gui.enterbox(
    msg="Introduce the end page to extract",
)

#  If the user does not enter an ending page number, exit the program.

if end_page == "" or end_page is None:
    exit()

# If the user enters an invalid page number:

end_page = page_validator(end_page)

# Ask for the location to save the extracted pages.
default_name = f"{basename(path_to_pdf).strip('.pdf')} slice.pdf"
save_path = gui.filesavebox(
    title="Save file to",
    default=default_name
)
#  If the user does not select a save location, exit the program.

if save_path == "" or save_path is None:
    exit()

# If the chosen save location is the same as the input file path.

while save_path == path_to_pdf:
    gui.msgbox(
        msg="You can not overdrive the old file with the new file.",
        title="Warning!!!"
    )
    save_path = gui.filesavebox(
        title="Save file to",
        default=default_name
    )

pdf_reader = PdfFileReader(path_to_pdf)
pdf_writer = PdfFileWriter()

for page in pdf_reader.pages[start_page - 1:end_page]:
    pdf_writer.addPage(page)

with open(save_path, mode="wb") as output_file:
    pdf_writer.write(output_file)

gui.msgbox(
    msg="Task Completed",
    title="Information"
)
