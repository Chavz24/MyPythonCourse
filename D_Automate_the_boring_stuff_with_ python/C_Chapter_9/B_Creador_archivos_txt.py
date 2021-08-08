#Este programa va a un folder  en  en el disco F, si el subfolder  que se
#quiere usar no esta en el folder se crea el subfolder  y los archivos de
#texto que este va contener, si el subfolder  esta creado, este crea solo
#los archivos de texto.

from  pathlib import Path
from datetime import  datetime
import os

folder=Path(r'F:/Documentos Practica Python/2-crear_archivos')
if folder.exists():
    pass
else:
    folder=Path(r'F:/Documentos Practica Python/2-crear_archivos').mkdir()


print(folder.parent)
folder=os.path.basename(folder)
print(folder)



for i in range (4):
    nombre_archivo=input("Digite el nombre del archivo:")
    archivo_nuevo=open(f"F:/Documentos Practica Python/{folder}/{nombre_archivo}.txt",'w')
    archivo_nuevo.write(datetime.today().strftime(f'%d/%m/%y/ Dia %j %H %M %S %p'))