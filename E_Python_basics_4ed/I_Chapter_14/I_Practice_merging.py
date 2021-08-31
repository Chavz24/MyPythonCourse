"""Review Exercises 14.4"""

from PyPDF2 import PdfFileMerger
from pathlib import Path

# In the Chapter 14 Practice Files directory there are three PDFs
# called merge1.pdf, merge2.pdf, and merge3.pdf. Using a PdfFileMerger
# instance, concatenate the two files merge1.pdf and merge2.pdf using
# .append()


# path_to_files = Path()
#
# pdf_merger = PdfFileMerger()
# pdf_to_merge = [path for path in path_to_files.glob('*.pdf') if not path.name == 'merge3.pdf']
#
# for path in pdf_to_merge:
#     pdf_merger.append(str(path))
#
# with open('II_concatenated.pdf', mode='wb') as file:
#     pdf_merger.write(file)

# With a new PdfFileMerger instance, use .merge() to merge the file
# merge3.pdf in-between the two pages in the concatenated.pdf file
# you made in exercise 1. Save the new file to your home directory
# as merged.pdf.

path_to_file = Path()

pdf_to_merge = Path()

pdf_merger = PdfFileMerger()
pdf_merger.append(str(path_to_file))
pdf_merger.merge(1, str(pdf_to_merge))

with open('II_merged.pdf', mode='wb') as file:
    pdf_merger.write(file)
