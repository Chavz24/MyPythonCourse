


import docx

import PyPDF2


"""Uso esto para convertir la direcion del archivo estilo window a estilo unix"""

path_win_list=[r'C:\Users\migue\PycharmProjects\MyPythonCourse\Z_archivos\automate_online-materials\demo.docx']
path_unix_list=[]
for path in path_win_list:
    dir_list=path.split('\\')
    unix_path='/'.join(dir_list)
    path_unix_list.append(unix_path)
#print(path_unix_list)

#Esta funcion retorna to' el texto en un documento que se le pase por parametro
def get_text(filename):
    doc=docx.Document(filename)
    all_text=[]
    for paragraph in doc.paragraphs:
        all_text.append(paragraph.text)
    return '\n'.join(all_text)

print(get_text(path_unix_list[0]))