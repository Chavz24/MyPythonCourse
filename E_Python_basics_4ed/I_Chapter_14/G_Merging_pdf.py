from PyPDF2 import PdfFileMerger
from pathlib import Path

path1 = Path()

pdf_merger = PdfFileMerger()

paths_list = [path for path in path1.glob('*.pdf')]
paths_list.sort()

for path in paths_list:
    pdf_merger.append(str(path))

with (Path.cwd() / f'GG_{path1.name}.pdf').open(mode='wb') as file:
    pdf_merger.write(file)
