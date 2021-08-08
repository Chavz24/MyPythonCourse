"""Este scrip crea un folder en un folder del disco F:/( el nombre del folder debe ser
    pasado como parametro a la funcion'backptozip' junto con la direcion del folder
    del cual se quiere hacer el backup, como segundo parametro"""

import zipfile,os
from pathlib import  Path


def creadorFolder(nombrefolder):
    """Esta funcion crea el folder del backup"""

    folder_trabajo = Path(f"F:/Documentos Practica Python/{nombrefolder}")

    if folder_trabajo.exists():
        pass
    else:
        print(f'Creando backup folder {nombrefolder}...')
        os.makedirs(folder_trabajo)
    return os.path.abspath(folder_trabajo)



def backuptozip(backupFolder,backingFolder):
    """Esta funcion crea un backup del folder y de sus archivos que se le pase como parametro"""


    backup_folder=os.path.abspath(creadorFolder(backupFolder))
    backing_folder=os.path.abspath(backingFolder)


    back_up_file_number=1
    while True:
        zip_file_name=os.path.basename(backing_folder)+'_'+str(back_up_file_number)+'.zip'
        if not os.path.exists(f'{backup_folder}/{zip_file_name}'):
            break
        back_up_file_number+=1

    """Creando archivo zip"""

    print(f"Creando {zip_file_name}....")
    backup_zip=zipfile.ZipFile(f'{backup_folder}/{zip_file_name}','w')

    for folder_name,subfoleder_names,files_names in os.walk(backing_folder):
        print(f"Agregando archivos en {folder_name}...")
        backup_zip.write(folder_name)

        for file in files_names:
            new_base=os.path.basename(backing_folder)+'_'
            if file.startswith(new_base) and file.endswith('.zip'):
                continue
            backup_zip.write(os.path.join(folder_name,file))
    backup_zip.close()

    return print('Tarea terminada')


backuptozip('6-Practica_2_Capitulo_10','F:/Documentos Practica Python/5-proyecto_capitulo_10')

