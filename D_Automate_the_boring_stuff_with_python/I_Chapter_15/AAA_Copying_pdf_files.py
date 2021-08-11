

import PyPDF2
"""Uso esto para convertir la direcion del archivo estilo window a estilo unix"""

path_win_list=[r'C:\Users\migue\PycharmProjects\MyPythonCourse\Z_archivos\automate_online-materials\meetingminutes.pdf'
               ,r'C:\Users\migue\PycharmProjects\MyPythonCourse\Z_archivos\automate_online-materials\meetingminutes2.pdf']
path_unix_list=[]
for path in path_win_list:
    dir_list=path.split('\\')
    unix_path='/'.join(dir_list)
    path_unix_list.append(unix_path)


pdf_file1=PyPDF2.PdfFileReader(open(path_unix_list[0],'rb'))
pdf_file2=PyPDF2.PdfFileReader(open(path_unix_list[1],'rb'))

new_pdf=PyPDF2.PdfFileWriter()

for page_num in range(pdf_file1.numPages):
    page=pdf_file1.getPage(page_num)
    new_pdf.addPage(page)
for page_num in range(pdf_file2.numPages):
    page=pdf_file2.getPage(page_num)
    new_pdf.addPage(page)

new_pdf_file=open('AAA_Unite.pdf','wb')
new_pdf.write(new_pdf_file)
new_pdf_file.close()
