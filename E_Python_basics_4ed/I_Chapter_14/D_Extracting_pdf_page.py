import PyPDF2
from pathlib import Path

path_pdf_file = Path.cwd() / 'DD_Pride_and_Prejudice.pdf'
path = ()

pdf_reader = PyPDF2.PdfFileReader(path)
pdf_writer = PyPDF2.PdfFileWriter()

# page = pdf_reader.getPage(0)
# pdf_writer.addPage(page)
#
# with path_pdf_file.open(mode='wb') as pdf_file:
#     pdf_writer.write(pdf_file)

chapter1 = Path.cwd() / 'DD_Pride_and_Prejudice_Ch1.pdf'

for page in pdf_reader.pages[1:4]:
    pdf_writer.addPage(page)
with chapter1.open(mode='wb') as chapter:
    pdf_writer.write(chapter)

