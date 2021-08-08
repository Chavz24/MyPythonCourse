# Este progrma abre una archivo de texto, cambia las palabras en el regex
#por las qque le india el user y crea una copia modificada en el escritorio

import re

regex=re.compile(r'ADJETIVO|VERBO|PROPIO|ADVERVIO')
poema_neruda=open(f'F:/Documentos Practica Python/Ejercicio 2 capitulo 9, Automate/NERUDA.txt','r')

nuevo_poema=open(f'C:/Users/migue/Desktop/NERUDA2.txt','w')

linea_poemas=poema_neruda.readlines()

for linea in  linea_poemas:

    if regex.findall(linea):
        palabra=regex.findall(linea)
        #Esta linea usa el metodo regex.sub para sustituir la palabra que coincide dentro delregex con
        #la que el usuario debe ingresar.
        nuevo_poema.write(regex.sub(str(input(f'Ingrese un {palabra[0]}:'
                          )).upper(),linea))
    else:
        nuevo_poema.write(f'{linea}')

poema_neruda.close()

nuevo_poema=open(f'C:/Users/migue/Desktop/NERUDA2.txt','r')
print(nuevo_poema.read())
nuevo_poema.close()





