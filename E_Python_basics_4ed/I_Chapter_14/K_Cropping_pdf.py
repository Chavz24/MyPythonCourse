from copy import deepcopy
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

path_to_file = Path()

pdf_reader = PdfFileReader(str(path_to_file))
pdf_writer = PdfFileWriter()

for page in pdf_reader.pages:

    left_side = deepcopy(page)
    right_side = deepcopy(page)

    current_coords = left_side.mediaBox.upperRight
    new_coords = (current_coords[0] / 2, current_coords[1])

    left_side.mediaBox.upperRight = new_coords
    pdf_writer.addPage(left_side)

    right_side.mediaBox.upperLeft = new_coords
    pdf_writer.addPage(right_side)


with open('KK_cropped.pdf', mode='wb') as file:
    pdf_writer.write(file)
