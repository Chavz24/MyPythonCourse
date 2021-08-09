# descargar cada xkcd comic.

import requests,bs4,os,logging

open('mylog.txt','w').write('\n')
logging.basicConfig(filename='mylog.txt',level=logging.DEBUG,format='%(asctime)s- %(levelname)s-%(message)s')
logging.disable(logging.CRITICAL)



url='https://xkcd.com'
os.makedirs('xkcd',exist_ok=True)

while not url.endswith('#'):
    print(f'Descargando imagenes desde {url}')
    res=requests.get(url)
    res.raise_for_status()

    soup=bs4.BeautifulSoup(res.text,'html.parser')

    imagen=soup.select('#comic img')
    print(imagen)

    if imagen==[]:
        print(f'No se encontratron imagenes en este enlace {url}')
    else:
        url_imagen='https:'+ imagen[0].get('src')
        print(f'Descargando imagen {url_imagen}')
        res=requests.get(url_imagen)
        res.raise_for_status()

        img_file=open(os.path.join('xkcd',os.path.basename(url_imagen)),'wb')
        for i in res.iter_content(100000):
            img_file.write(i)
        img_file.close()

    prev_botton=soup.select('a[rel="prev"]')[0]
    logging.debug(f'Prev botton link {prev_botton}')
    url='https://xkcd.com'+ prev_botton.get('href')
    logging.debug(f'Nuevo url es {url}')


print('Terminado')
