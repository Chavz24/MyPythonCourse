""" Challenge: PdfFileSplitter Class 14.3"""

# Create a class called PdfFileSplitter that reads a PDF from an existing
# PdfFileReader instance and splits the PDF into two new PDFs.

from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path


class PdfFileSplitter():

    def __init__(self, path):
        self.reader = PdfFileReader(path)
        self.writer1 = PdfFileWriter()
        self.writer2 = PdfFileWriter()


    def __num_pages(self):
        return self.reader.getNumPages()

    def spliter(self, breakpoint=int()):
        try:
            if (not self.__num_pages() <= breakpoint) and breakpoint>0:
                for page in self.reader.pages[:breakpoint]:
                    self.writer1.addPage(page)
                for page in self.reader.pages[breakpoint:]:
                    self.writer2.addPage(page)
            else:
                if breakpoint>0:
                    print(f'Breakpoint page value is greater than number of pages in {Path(path).name}.')
                else:
                    print(f'Breakpoint page value can not be 0.')
        except TypeError:
            print('Breakpoint must be an interger.')

    def writer(self, filename=str()):
        if not (self.writer1.getNumPages() == 0 and self.writer2.getNumPages() == 0):
            path1 = Path.cwd() / f'{filename}1.pdf'
            path2 = Path.cwd() / f'{filename}2.pdf'
            with path1.open('wb') as file1:
                self.writer1.write(file1)
            with path2.open('wb') as file2:
                self.writer2.write(file2)


path_pdf_file = 'FF_Part'
path = ()

try:
    pdf_to_split = PdfFileSplitter(path)
    pdf_to_split.spliter(6)
    pdf_to_split.writer(path_pdf_file)
    # print(pdf_to_split._PdfFileSplitter__num_pages())  # this is the way to access a private method.
except TypeError:
    print('PdfFileSpliter missing path_to_pdf.')
except NameError:
    print('An error ocurred')





