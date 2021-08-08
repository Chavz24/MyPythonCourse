

from pathlib import Path
import shutil, os, zipfile

#shiroi_kage.ogg

#folder1=Path(r'F:/Documentos Practica Python/2-crear_archivos')

folder2=Path(r'F:/Documentos Practica Python/3-crear_folder/1-crear_archivos')
# print(folder2.parents[0])
#os.makedirs(folder2)

# shutil.copy(folder1/'prueba1.txt',folder2/'prueba5.txt')
#
# shutil.copytree(folder2,folder1/'backup')
#shutil.rmtree(folder2.parents[0]) #borra un path y todos los subfolders y archivos.

# for archivo in folder2.parent.glob('*'):
#     print(archivo)

## Usando os.walk para imprimir los nombres de los folders, subfordels y archivos en un path

# for foldername,subfolders,files in os.walk('F:/Documentos Practica Python'):
#     print('El folder actual es: ',foldername)
#     for subfolder in subfolders:
#         print(subfolder+' **esta dendro de ** '+foldername)
#     for file in files:
#         print(file+ ' ***esta dendro de*** '+foldername)

##Comprimiendo archivos con la funcion ZIP

print(folder2.parents[1])

print(Path(folder2.parents[1]/'BGM.zip'))

archivo_zip=zipfile.ZipFile(folder2.parents[1]/'BGM.zip')

print(archivo_zip.namelist()[archivo_zip.namelist().index('BGM/shiroi_kage.ogg')])

## creando una lista de toos los archivos dentro de zip.
# for file in archivo_zip.namelist():
#     print(file.strip(('.ogg')).strip('BGM/'))

##extrating informacion de archivos dentro del zip
# BGM_info=archivo_zip.getinfo(archivo_zip.namelist()[2])
# print(BGM_info.file_size)
# print(BGM_info.compress_size)
# print(f'T {round(BGM_info.file_size/BGM_info.compress_size)}x smaller')

##Extrating todos los archivos de un zip en un folder
#archivo_zip.extractall('F:/Documentos Practica Python/3-crear_folder')

##Extrating un archivo especifico desde un archivo .zip

#archivo_zip.extract('BGM/shiroi_kage.ogg','F:/Documentos Practica Python')


## Comprimiendo un archivo

nuevo_archivo_zip=zipfile.ZipFile('F:/Documentos Practica Python/Umineko1.zip','w')
nuevo_archivo_zip.write('F:/Documentos Practica Python/BGM/shiroi_kage.ogg',compress_type=zipfile.ZIP_DEFLATED)
nuevo_archivo_zip.close()


















