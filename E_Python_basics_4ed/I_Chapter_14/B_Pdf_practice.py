"""Review Exercises 14.1"""

import PyPDF2

path=()

# In the Chapter 14 Practice Files directory there is a PDF file called
# zen.pdf. Create a PdfFileReader from this PDF.

pdf_file=PyPDF2.PdfFileReader(path)

# Using the PdfFileReader instance from Exercise 1, print the total
# number of pages in the PDF.

print(pdf_file.getNumPages())

# Print the text from the first page of the PDF in Exercise 1.

page=pdf_file.getPage(0)
text=page.extractText()
print(text)