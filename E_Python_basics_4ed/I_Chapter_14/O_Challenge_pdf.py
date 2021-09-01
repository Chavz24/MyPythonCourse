""" Challenge: Unscramble A PDF 14.7"""

from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

# Write a script that unscrambles the PDF by sorting the pages according to
# the number contained in the page text and rotating the page, if needed, so that it is upright.

path_to_file = Path()

pdf_reader = PdfFileReader(str(path_to_file))
pdf_writer = PdfFileWriter()
pdf_reader.getDocumentInfo()
page_list = []
count = 1
while count <= pdf_reader.getNumPages():
    for page in pdf_reader.pages:
        for char in page.extractText():
            if char == str(count):
                page_list.append(page)
    count += 1

for page in page_list:
    if page['/Rotate'] > 0:
        rotate = page['/Rotate']
        page.rotateCounterClockwise(rotate)
    elif page['/Rotate'] < 0:
        rotate = page['/Rotate']
        page.rotateCounterClockwise(rotate)
    pdf_writer.addPage(page)

with open('OO_unscrambled.pdf', mode='wb') as file:
    pdf_writer.write(file)
