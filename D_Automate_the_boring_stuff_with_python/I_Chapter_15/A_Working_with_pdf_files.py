##C:\Users\migue\PycharmProjects\MyPythonCourse\Z_archivos\automate_online-materials\meetingminutes.pdf
#C:\Users\migue\PycharmProjects\MyPythonCourse\Z_archivos\automate_online-materials\combinedminutes.pdf

import PyPDF2
"""Uso esto para convertir la direcion del archivo estilo window a estilo unix"""
string=r'C:\Users\migue\PycharmProjects\MyPythonCourse\Z_archivos\automate_online-materials\meetingminutes.pdf'
list1=string.split('\\')
string2='/'.join(list1)


pdf_file=open(string2,'rb')
read_pdf=PyPDF2.PdfFileReader(pdf_file)
pages=read_pdf.numPages

page=read_pdf.getPage(0)
print(page.extractText())




