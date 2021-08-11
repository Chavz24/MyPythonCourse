

import PyPDF2
"""Uso esto para convertir la direcion del archivo estilo window a estilo unix"""

path_win_list=[r'C:\Users\migue\PycharmProjects\MyPythonCourse\Z_archivos\automate_online-materials\meetingminutes.pdf'
               ,r'C:\Users\migue\PycharmProjects\MyPythonCourse\Z_archivos\automate_online-materials\watermark.pdf']
path_unix_list=[]
for path in path_win_list:
    dir_list=path.split('\\')
    unix_path='/'.join(dir_list)
    path_unix_list.append(unix_path)

pdf_obj=open(path_unix_list[0],'rb')
pdf_file=PyPDF2.PdfFileReader(pdf_obj)
page=pdf_file.getPage(0)
pdf_watermark=PyPDF2.PdfFileReader(open(path_unix_list[1],'rb'))
page.mergePage(pdf_watermark.getPage(0))
new_pdf=PyPDF2.PdfFileWriter()
new_pdf.addPage(page)

for page_num in range(1,pdf_file.numPages):
    page_obj=pdf_file.getPage(page_num)
    new_pdf.addPage(page_obj)

final_pdf_file=open('B_Watermarked.pdf','wb')
new_pdf.write(final_pdf_file)
final_pdf_file.close()
pdf_obj.close()