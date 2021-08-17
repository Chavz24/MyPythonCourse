
"""Este programa busca en todos los folders del disco C:\ por imagenes mayores a 500x500 y si en dicho folder
    mas de la mitad de los archivos son imagenes, imprime el path del folder"""

import os,time
from PIL import Image

start_time=time.time()
for folder_name,subfolder_name,file_names in os.walk('C:/'):
    numero_archivos=0
    numero_imagenees=0
    imagenes_por_folder=[]
    for file_name in file_names:
        #si el archivo no tiene una de estas ext, salta al siguiente archivo
        if not file_name.endswith(('.png',".PNG",'.jpg','.JPG','.GIF','.gif','.bmp','.BMP','.jpeg','.JPEG')):
            numero_archivos+=1
            continue
        #por alguna razon no abre los archivos si no le paso el absolute path
        img_dir=(folder_name+'\\'+file_name).split('\\')
        new_dir='/'.join(img_dir)

        #este try es porque intenta abrir archivos del sistema
        try:
            img=Image.open(new_dir)
            # si el archivo es mayor 500x500 lo cuenta como imagen
            if img.size > (500, 500):
                numero_imagenees += 1
                imagenes_por_folder.append(file_name)
            else:
                numero_archivos += 1

        except:
            continue

    if numero_imagenees>(numero_archivos/2):
        print(folder_name)

end_time=time.time()

print(f'Se a tardo {round(end_time-start_time,2)} segundos en realizar la busqueda')