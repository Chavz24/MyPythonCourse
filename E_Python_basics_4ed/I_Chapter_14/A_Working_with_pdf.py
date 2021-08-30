import PyPDF2
from pathlib import Path

path_txt_file=Path.cwd()/'AA_Pride_and_Prejudice.txt'
path=()

pdf_reader=PyPDF2.PdfFileReader(path)

with path_txt_file.open(mode='a', encoding='utf-8') as file:

     file.write(f'{pdf_reader.documentInfo.title}\n'
                f'{pdf_reader.getNumPages()}\n\n')

     for page in pdf_reader.pages:
          text=page.extractText()
          file.write(text)



