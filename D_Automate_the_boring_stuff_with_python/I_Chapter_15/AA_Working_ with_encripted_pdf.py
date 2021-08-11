

import PyPDF2
"""Uso esto para convertir la direcion del archivo estilo window a estilo unix"""
string=r'C:\Users\migue\PycharmProjects\MyPythonCourse\Z_archivos\automate_online-materials\encrypted.pdf'
list1=string.split('\\')
string2='/'.join(list1)


pdf_file=PyPDF2.PdfFileReader(open(string2,'rb'))
pdf_file.decrypt('rosebud')

page=pdf_file.getPage(1)
print(page.extractText())

