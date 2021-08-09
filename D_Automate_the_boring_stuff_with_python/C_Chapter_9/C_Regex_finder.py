#Abre todos los archivos *.txt en un folder y los lee para buscar una coincidencia
#con el regex que se le pasa e imprime esta coincidencia en pantalla.

from re import compile
from pathlib import Path
import os

fecha=compile(r'\d\d/\d\d/\d\d')
folder=Path(r'F:/Documentos Practica Python/2-crear_archivos')


for archivo in folder.glob('*.txt'):
    abrir_archivo=open(archivo,'r')
    for linea in abrir_archivo:
        if fecha.findall(linea):
            dato =''.join(fecha.findall(linea))
            print(f"Nombre del archivo:{os.path.basename(archivo)},Dato buscado: {dato}")

    abrir_archivo.close()




