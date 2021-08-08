#Este programa recorre un grupo de archivos en un folder e inserta un salto en la numeracion
#

import os,re,shutil,pyinputplus as pyip
from pathlib import  Path



def creadorFolder(nombrefolder):
    """Esta funcion crea el folder del backup"""

    folder_trabajo = Path(f"F:/Documentos Practica Python/{nombrefolder}")

    if folder_trabajo.exists():
        pass
    else:
        print(f'Creando backup folder {nombrefolder}...')
        os.makedirs(folder_trabajo)
        print(f'Listo')
    return os.path.abspath(folder_trabajo)


folder_trabajo=creadorFolder('8-Practica_4_cap_10')


"""Este bucle crea los archivos para la practica"""
# for i in range(1,21):
#     nuevo_archivo=open(f"{folder_trabajo}/archivos"
#                        f"{'0'*(3-len(str(i)))+str(i)}.txt",'a')
#     nuevo_archivo.write(f' archivo_de_trabajo {f"{i}"}{i+100}')


numeracion_re = re.compile(r"""^(.*?)(\d{1,})(.*?)$""", re.VERBOSE)

find=pyip.inputStr("Ingrese una numeracion en formato 000 del archivo a buscar:",
                   allowRegexes=[r'(^\d{1,}$)'],
                   blockRegexes=[('.*', 'Formato incorrecto')])

count=0

for file in Path(f'{folder_trabajo}').glob('*.???'):
    file_name=os.path.basename(file)

    buscar_numero=numeracion_re.search(file_name)

    if buscar_numero==None:
        continue

    count+=1
    new_name=(f'{buscar_numero.group(1)}{"0"*(3-len(str(count+1)))+str(count+1)}.txt')

    check_file=Path(f'{folder_trabajo}/new_files/{buscar_numero.group()}').exists()

    if find != buscar_numero.group(2) and check_file == False:
        shutil.move(f'{folder_trabajo}/{file_name}',
                    f'{folder_trabajo}/new_files/')

    elif find==buscar_numero.group(2)and check_file==False:
        shutil.move(f'{folder_trabajo}/{file_name}',
                    f'{folder_trabajo}/new_files/{new_name}')

    else:
        shutil.move(f'{folder_trabajo}/{file_name}',
                    f'{folder_trabajo}/new_files/{new_name}')





