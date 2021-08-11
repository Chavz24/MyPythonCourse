

import PyPDF2,os
from pathlib import Path
"""Uso esto para convertir la direcion del archivo estilo window a estilo unix"""

# path_win_list=[r'C:\Users\migue\PycharmProjects\MyPythonCourse\Z_archivos\automate_online-materials\meetingminutes.pdf'
#                ,r'C:\Users\migue\PycharmProjects\MyPythonCourse\Z_archivos\automate_online-materials\watermark.pdf']
# path_unix_list=[]
# for path in path_win_list:
#     dir_list=path.split('\\')
#     unix_path='/'.join(dir_list)
#     path_unix_list.append(unix_path)

##step1
pdf_files=[]
for folder,subfolders,files in os.walk('C:/Users/migue/Desktop/practica'):
    for file in files:
       if file.endswith('.pdf'):
        pdf_files.append(os.path.join(folder,file))

#step1.1:make the paths unix stile
path_unix_list=[]
for path in pdf_files:
    dir_list=path.split('\\')
    unix_path='/'.join(dir_list)
    path_unix_list.append(unix_path)

path_unix_list.sort(key=str.lower)
new_pdf=PyPDF2.PdfFileWriter()
print(path_unix_list[73])

# for file in path_unix_list[75:168]:
#     try:
#         pdf_obj=open(file,'rb')
#         pdf_file=PyPDF2.PdfFileReader(pdf_obj,strict=False)
#
#         for page_num in range(1,pdf_file.numPages):
#             page=pdf_file.getPage(page_num)
#             new_pdf.addPage(page)
#     except:
#         continue
#
# final_pdf_file=open('CC_allmypdf3.pdf','wb')
# new_pdf.write(final_pdf_file)
# final_pdf_file.close()



