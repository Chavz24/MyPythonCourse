from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

path_to_file = Path()

pdf_reader=PdfFileReader(str(path_to_file))
pdf_writer=PdfFileWriter()

pdf_writer.appendPagesFromReader(pdf_reader)
pdf_writer.encrypt(user_pwd='SuperSecret',owner_pwd='ReallySuperSecret')

with open('MM_encrypted.pdf',mode='wb') as file:
    pdf_writer.write(file)

# Decrypting

path_to_file=Path.cwd()/'MM_encrypted.pdf'

pdf_reader=PdfFileReader(str(path_to_file))

print(pdf_reader.decrypt(password='SuperSecret'))
pdf_reader.decrypt(password='SuperSecret')





