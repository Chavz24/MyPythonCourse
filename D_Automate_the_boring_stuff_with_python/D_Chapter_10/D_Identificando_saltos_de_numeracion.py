
import os,re,shutil
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


folder_trabajo=creadorFolder('7-Practica_3_cap_10')



"""Este bucle crea los archivos para la practica"""
# for i in range(1,21):
#     nuevo_archivo=open(f"{folder_trabajo}/archivos"
#                        f"{'0'*(3-len(str(i)))+str(i)}.txt",'a')
#     nuevo_archivo.write(f' archivo_de_trabajo {f"{i}"}{i+100}')


for file in Path(f'{folder_trabajo}').glob('*.???'):
    print(os.path.basename(file))


numeracion_re = re.compile(r"""^(.*?)(\d{1,})(.*?)$""", re.VERBOSE)

numero_archivo_anterior=0
count=0

for file in os.listdir(folder_trabajo):

    patron_numero_re= numeracion_re.search(file)
    if patron_numero_re==None:
        continue
    archivo_actual=patron_numero_re.group(2)

    if '0' in patron_numero_re.group(2):
        numero_archivo_actual=int(archivo_actual.lstrip('0'))

        if (numero_archivo_anterior-numero_archivo_actual)<-1:
            print(f'Falta un archivo aqui')
           # print(file)
        else:
            print(file)

        numero_archivo_anterior=numero_archivo_actual

    count+=1
    nombre_nuevo=str(f"archivos{'0'*(3-len(str(count)))+str(count)}.txt")


    shutil.move(f'{folder_trabajo}/{file}',
               f'{folder_trabajo}/now/{nombre_nuevo}')

