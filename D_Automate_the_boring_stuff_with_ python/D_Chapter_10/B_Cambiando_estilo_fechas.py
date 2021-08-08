import os
from pathlib import Path
import re
from random import randint
import datetime
import shutil

# creando el directorio para trabajar
folder_trabajo = Path(r'F:/Documentos Practica Python/5-proyecto_capitulo_10')

if folder_trabajo.exists():
    pass
else:
    os.makedirs(folder_trabajo)
# creando los archivos a trbajar, estos son archivos con fecha estilo americana MM/DD/AAAA

# folder_trabajo=os.path.basename(folder_trabajo)


# for i in range(55):
#     mes=randint(1,12)
#     dia=randint(1,31)
#     ano=randint(1990,2021)
#     fecha=(datetime.date(ano,mes,dia).strftime(f'%m-%d-%Y'))
#     nuevo_archivo=open(f"F:/Documentos Practica Python/{folder_trabajo}/mas archivos{i}.txt",'a')
#     nuevo_archivo.write(f'archivo de trabajo {i}')


##Creando un regex para buscar los archivos con fechas

fechas_americanas = re.compile(r"""^(.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20)?\d\d)
(.*?)$""", re.VERBOSE)

##Listando los archivos dentro del folder_trabajo

for file in os.listdir(folder_trabajo):
    print(file)
    files_with_american_dates = fechas_americanas.search(file)

    if files_with_american_dates == None:
        continue

    # print(files_with_american_dates.group(8))
    nombre_archivos = files_with_american_dates.group(1)
    mes = files_with_american_dates.group(2)
    dia = files_with_american_dates.group(4)
    ano = files_with_american_dates.group(6)
    extension = files_with_american_dates.group(8)
    #print(extension)

    files_with_european_dates = nombre_archivos + dia + '-' + mes + '-' + ano + extension
    #print(files_with_european_dates)

    # esta linea mueve los archivos con fechas americanas a otras carpeta y les cambia la fecha por el estilo
    #europeo.
    shutil.move(f"{folder_trabajo}/{file}",
                f"{folder_trabajo}/New/{files_with_european_dates}")
