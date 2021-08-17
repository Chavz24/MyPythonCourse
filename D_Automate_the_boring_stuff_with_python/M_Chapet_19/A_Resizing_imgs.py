"""Este programa reajusta el tamano de las imagenes en un directorio y les imprime un logo en las
    cuatro esquinas"""
import os
from PIL import Image

new_size=800
logo='AA_catlogo.png'

logo_img=Image.open(logo)
ancho_logo,alto_logo=logo_img.size

os.makedirs('logo_img',exist_ok=True)
for img in os.listdir('.'):
    if not (img.endswith('.png') or img.endswith('.jpg')) or img==logo:
        continue

    imagen=Image.open(img)
    ancho,alto=imagen.size

    #Revisando si la imagentienr que ser reajustada
    if ancho>new_size and alto>new_size:
        # calculando el nuevo ancho y alto
        if ancho>alto:
            alto=int((new_size/ancho)*alto)
            ancho=new_size
        else:
            ancho=int((new_size/alto)*ancho)
            alto=new_size
        print(f'Reajustanto el tamano de la imagen {img}...')
        imagen=imagen.resize((ancho,alto))
    print(f'Anadiendo logo a {img}...')
    #esta line imprime el logo en la esquina superior izquierda
    imagen.paste(logo_img,(ancho-int(ancho_logo*int(ancho/ancho_logo)),0),logo_img)
    #esta linea imprime el logo en la esquina inferior derecha
    imagen.paste(logo_img, (ancho - ancho_logo, alto - alto_logo), logo_img)
    #esta linea imprime el logo en la esquina superior derecha
    imagen.paste(logo_img, (ancho - ancho_logo, 0), logo_img)
    #esta line imprime el logo en la esquina inferior izquierda
    imagen.paste(logo_img, (ancho - int(ancho_logo * int(ancho / ancho_logo)),alto-alto_logo),logo_img)

    imagen.save(os.path.join('logo_img',img))



