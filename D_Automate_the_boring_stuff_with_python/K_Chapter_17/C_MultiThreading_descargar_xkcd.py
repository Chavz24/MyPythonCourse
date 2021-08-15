"""Este programa descarga imagenes del sitio xkcd.com usando multi threading"""

import requests,bs4,os,logging,threading

open('mylog.txt','w').write('\n')
logging.basicConfig(filename='mylog.txt',level=logging.DEBUG,format='%(asctime)s- %(levelname)s-%(message)s')
logging.disable(logging.CRITICAL)

url='https://xkcd.com'
os.makedirs('xkcd',exist_ok=True)


def download_xkcd(star_number,end_number):
    for url_number in range(star_number,end_number):
        #Dowloading la pagina
        print(f'Descargando la pagina {url}/{url_number}...')
        res=requests.get(f'{url}/{url_number}')
        res.raise_for_status()

        soup=bs4.BeautifulSoup(res.text,'html.parser')

        #Link del comic
        comic_link=soup.select('#comic img')
        if comic_link==[]:
            print(f'No se encontro ninguna imagen {comic_link[0]}')
        else:
            url_comic=comic_link[0].get('src')
            print(f'Descargando imagen {url_comic}')
            res=requests.get('https:'+url_comic)
            res.raise_for_status()

            #guardando imagen

            imagen=open(os.path.join('xkcd',os.path.basename(url_comic)),'wb')
            for i in res.iter_content(100000):
                imagen.write(i)
            imagen.close()

hilos_de_descarga=[]
for i in range(0,140,10):
    start=i
    end=i+9
    if start==0:
        start=1

    hilo_descarga=threading.Thread(target=download_xkcd,args=(start,end))
    hilos_de_descarga.append(hilo_descarga)
    hilo_descarga.start()


for hilo_descarga in hilos_de_descarga:
    hilo_descarga.join()

print('Terminado')