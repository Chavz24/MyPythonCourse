"""Review Exercises 14.5"""
from copy import deepcopy
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

# In the Chapter 14 Practice Files folder there is a PDF called
# split_and_rotate.pdf. Create a new PDF called rotated.pdf in
# your home directory containing the pages of split_and_rotate.pdf
# rotated counterclockwise 90 degrees.


path_to_file = Path()

pdf_reader = PdfFileReader(str(path_to_file))
pdf_writer = PdfFileWriter()

for page in pdf_reader.pages:
    if page['/Rotate'] == 90:
        page.rotateCounterClockwise(90)
    pdf_writer.addPage(page)

with open('LL_rotated.pdf', mode='wb') as file:
    pdf_writer.write(file)

# Using the rotated.pdf file you created in exercise 1, split each page
# of the PDF vertically in the middle. Create a new PDF called
# split.pdf in your home directory containing all of the split pages.

path_to_file = Path.cwd() / 'LL_rotated.pdf'

pdf_reader = PdfFileReader(str(path_to_file))
pdf_writer = PdfFileWriter()

for page in pdf_reader.pages:

    left_side = deepcopy(page)
    right_side = deepcopy(page)

    current_coords=left_side.mediaBox.upperRight
    new_coords=(current_coords[0]/2,current_coords[1])

    left_side.mediaBox.upperRight=new_coords
    pdf_writer.addPage(left_side)

    right_side.mediaBox.upperLeft=new_coords
    pdf_writer.addPage(right_side)

with open('LL_split.pdf',mode='wb') as file:
    pdf_writer.write(file)
