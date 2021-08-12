
"""Este programa encrypta y todos los archivos pdf que encuenta en un folder y sus subfolders
    y los renombra y borra los .pdf originales despues de encryptarlos"""

import PyPDF2,os

"""Uso esto para convertir la direcion del archivo estilo window a estilo unix"""


password=''
path='C:/Users/migue/Desktop/Practica'
pdf_list=[]
pdf_encritados=0
#listando todos los pdf en un directorio
for folder,subfolders,files in os.walk(path):
    for file in files:
       if file.endswith('.pdf'):
           pdf_list.append('/'.join(os.path.join(folder,file).split('\\')))

print(f'Se encontraron {len(pdf_list)} archivos pdf.')

#encriptando cada uno de los pdf en el folder
for pdf in pdf_list:
    #haciendo una copia de cada unos de los pdf eencontrados en el folder
    pdf_file=open(f'{pdf}','rb')
    pdf_obj=PyPDF2.PdfFileReader(pdf_file)
    encrypted_pdf=PyPDF2.PdfFileWriter()
    for page in range(pdf_obj.numPages):
        encrypted_pdf.addPage(pdf_obj.getPage(page))

    #Asignando un nuevo nombre al pdf
    new_name='_encrypted.'.join(pdf.split('.'))
    encrypted_pdf.encrypt(password)
    new_pdf=open(f'{new_name}','wb')
    encrypted_pdf.write(new_pdf)
    new_pdf.close()
    pdf_file.close()

    #Verificando si el nuevo archivo esta encriptado
    encrypted_file=open(new_name,'rb')
    encrypted_pdf_obj=PyPDF2.PdfFileReader(encrypted_file)
    if encrypted_pdf_obj.isEncrypted:
        print(f'El archivo {os.path.basename(pdf)} ha sido encriptado exitosamente')
        os.unlink(pdf)
        pdf_encritados+=1

print(f'Se han encritado {pdf_encritados} de {len(pdf_list)} pdf encontrados en {path}')
