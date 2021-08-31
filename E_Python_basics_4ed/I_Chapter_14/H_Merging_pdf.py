from PyPDF2 import PdfFileMerger
from pathlib import Path

path_to_files = Path()

path_to_report = path_to_files / 'report.pdf'
path_to_toc = path_to_files / 'toc.pdf'

pdf_merger = PdfFileMerger()
pdf_merger.append(str(path_to_report))
pdf_merger.merge(1, str(path_to_toc))

with (Path.cwd() / 'HH_Full_report.pdf').open(mode='wb') as file:
    pdf_merger.write(file)
