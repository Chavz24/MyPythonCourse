"""Este programa tomo todas los fotografias de un directorio y las cambia a blanco y negro y las
    guarda en una carpeta black and white"""
from PIL import Image, ImageEnhance
import os

#directorio de imagenes aqui
imgs=''

os.makedirs('./black and white',exist_ok=True)
#este bucle recorre todas la imagenes de la carpeta
for img in os.listdir(imgs):
    if not img.endswith(('.jpg','.JPG','.jpeg','.JPEG')):
        continue

    imagen=Image.open(imgs+'/'+img)
    #Escala de grises
    imagen=imagen.convert('L')

    imagen.save(os.path.join('',img))