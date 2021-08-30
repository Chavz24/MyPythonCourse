"""Review Exercises 14.2"""

from PyPDF2 import PdfFileWriter, PdfFileReader
from pathlib import Path

# Extract the last page from the Pride_and_Prejudice.pdf file and save
# it to a new file called last_page.pdf in your home directory.

path_pdf_file = Path.cwd() / 'EE_Last_page.pdf'
path = ()

pdf_reader = PdfFileReader(path)
last_page = pdf_reader.getPage(-1)

pdf_writer = PdfFileWriter()
pdf_writer.addPage(last_page)
with path_pdf_file.open(mode='wb') as page:
    pdf_writer.write(page)

# Extract all pages with even numbered indices from the Pride_-
# and_Prejudice.pdf and save them to a new file called every_other_-
# page.pdf in your home directory.

pdf_writer1 = PdfFileWriter()

for n in range(1, pdf_reader.getNumPages() - 1):
    if n % 2 == 0:
        page = pdf_reader.getPage(n)
        pdf_writer1.addPage(page)

path_pdf_file = Path.cwd() / 'EE_Every_other_page.pdf'

with path_pdf_file.open(mode='wb') as file:
    pdf_writer1.write(file)

# Split the Pride_and_Prejudice.pdf file into two new PDF files. The
# first file should contain the first 150 pages, and the second file
# should contain the remaining pages. Save both files in your home
# directory as part_1.pdf and part_2.pdf.

pdf_writer_part1 = PdfFileWriter()
pdf_writer_part2 = PdfFileWriter()

path_pdf_part1 = Path.cwd() / 'EE_Part1.pdf'
path_pdf_part2 = Path.cwd() / 'EE_Part2.pdf'

for page in pdf_reader.pages[:150]:
    pdf_writer_part1.addPage(page)

with path_pdf_part1.open(mode='wb') as part1:
    pdf_writer_part1.write(part1)


for page in pdf_reader.pages[150:]:
    pdf_writer_part2.addPage(page)
with path_pdf_part2.open(mode='wb') as part2:
    pdf_writer_part2.write(part2)

pdf_writer1.getPage(0)
