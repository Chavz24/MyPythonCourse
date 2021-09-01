from PyPDF2 import PdfFileWriter

pdf_writer = PdfFileWriter()

page = pdf_writer.addBlankPage(width=72, height=72)

with open('CC_blank.pdf', mode='wb') as pdf_file:
    pdf_writer.write(pdf_file)

