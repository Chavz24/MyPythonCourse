#Este programa hace una lsita de los nombres de todos los archivos
#con extension *.??? en un folder.

from pathlib import Path
import os
folder=Path(r'F:/Documentos Practica Python/2-crear_archivos')
nuevo_poema=open(f'C:/Users/migue/Desktop/NERUDA2.txt','w')
for archivo in folder.glob('*.???'):
    nuevo_poema.write(os.path.basename(archivo))
    nuevo_poema.write('\n')


nuevo_poema.close()
