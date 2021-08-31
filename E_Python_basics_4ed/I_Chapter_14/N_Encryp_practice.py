"""Review Exercises 14.5"""

from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

# In the Chapter 14 Practice Files folder there is a PDF file called
# top_secret.pdf. Using PdfFileWriter.encrypt(), encrypt the file with
# the user password Unguessable.

path_to_file = Path()

pdf_reader = PdfFileReader(str(path_to_file))
pdf_writer = PdfFileWriter()

pdf_writer.appendPagesFromReader(pdf_reader)

pdf_writer.encrypt(user_pwd='Unguessable')

with open('NN_top_secret_encrypted.pdf',mode='wb') as file:
    pdf_writer.write(file)


# Open the top_secret_encrpyted.pdf file you created in Exercise 1,
# decrypt it, and print the text contained on the first page of the PDF.

path_to_file=Path.cwd()/'NN_top_secret_encrypted.pdf'

pdf_reader=PdfFileReader(str(path_to_file))

pdf_reader.decrypt(password='Unguessable')


page=pdf_reader.getPage(0)
text=page.extractText()
print(text)

