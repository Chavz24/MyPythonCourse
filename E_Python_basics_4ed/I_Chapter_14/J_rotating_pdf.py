from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

path_to_file = Path()
pdf_reader = PdfFileReader(str(path_to_file))
pdf_writer = PdfFileWriter()

try:
    for page in pdf_reader.pages:
        if page["/Rotate"] == -90:
            page.rotateClockwise(90)

        pdf_writer.addPage(page)
except KeyError:
    print('Page has no key ["/Rotate"]')

with open('JJ_Rotated.pdf',mode='wb') as file:
    pdf_writer.write(file)
