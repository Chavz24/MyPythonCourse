"""Este programa reajusta el tamano de las imagenes en un directorio y les imprime un logo en las
    cuatro esquinas solo si el logo es tres veces mas grand que la imagen, reajusta el tamano del logo
    a una quinta parte del tamano de la imagen."""
import os
from PIL import Image

new_size=800
logo='AA_catlogo.png'

os.makedirs('logo_img',exist_ok=True)
for img in os.listdir('.'):
    logo_img = Image.open(logo)
    ancho_logo, alto_logo = logo_img.size
    if not (img.endswith(('.png',".PNG",'.jpg','.JPG','.GIF','.gif','.bmp','.BMP'))) or img==logo:
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

    #si la imagen es muy pequena en comparacion con el logo, reconfigura el tamano del logo a una 5 parte de la imagen
    if ancho<(ancho_logo*3) and alto<(alto_logo*3):
        if ancho_logo>alto_logo:
            alto_logo=int(((ancho/5)/ancho_logo)*alto_logo)
            ancho_logo=int(ancho/5)
        else:
            ancho_logo=int(((alto/5)/alto_logo)*ancho_logo)
            alto_logo=int(alto/5)
        logo_img=logo_img.resize((ancho_logo,alto_logo))

    print(f'Anadiendo logo a {img}...')

    #esta line imprime el logo en la esquina superior izquierda
    imagen.paste(logo_img,(ancho-int(ancho_logo*int(ancho/ancho_logo)),0),logo_img)

    #esta linea imprime el logo en la esquina inferior derecha
    imagen.paste(logo_img, (ancho - ancho_logo, alto - alto_logo), logo_img)

    #esta linea imprime el logo en la esquina superior derecha
    imagen.paste(logo_img, (ancho - ancho_logo, 0), logo_img)

    #esta line imprime el logo en la esquina inferior izquierda
    imagen.paste(logo_img, (ancho- int(ancho_logo * int(ancho / ancho_logo)),alto-alto_logo),logo_img)

    imagen.save(os.path.join('logo_img',img))
    logo_img.close()
