from PyPDF2 import PdfFileMerger
from pathlib import Path

path1 = Path('F:/A_Practicas_python/A_Python_basics_4ed/python-basics-exercises-master/ch14-interact-with-pdf-files/'
             'practice_files/expense_reports')

pdf_merger = PdfFileMerger()

paths_list = [path for path in path1.glob('*.pdf')]
paths_list.sort()

for path in paths_list:
    pdf_merger.append(str(path))

with (Path.cwd() / f'GG_{path1.name}.pdf').open(mode='wb') as file:
    pdf_merger.write(file)
