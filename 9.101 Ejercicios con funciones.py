#Crear un script que permita asignar una clave al nombre de las canciones de una lista para hacer una busqueda mas
#rapida de la cancion deseada.

#aqui podria ponerse un vinculo a una capeta y crear la lsita basado en los nombres de canciones dentro de ella
ListaCanciones= ['Welcome to the Jungle','Nightrain', 'Easy', 'My Michelle', 'Pradise City', 'SweetChild O \' Mine',
                 'Out ta Get Me', 'Mr. Brownstone', 'Think About You', 'You \' re Crazy', 'Anything Goes',
                 'Rocket Queen']
#Estas lista pordra crearse con las primeras letras del nombre de las canciones u otro metodo
ListaClaves=('wel','Nig','ez','my','ciy','sweet','out','mr','Think','crazy','goes','queen')
DictCanciones={}

def AsignadorClaves():
    #usando un for.... zip para crear un dict de canciones
    for claves,songs in zip(ListaClaves,ListaCanciones):
        #creando el dict
        DictCanciones[claves]=songs

#llamando la funcion
AsignadorClaves()

#creando una funcion para buscar las canciones en el dict
def BuscadorCanciones(Dict):
    Msj='y'
    while Msj=='y':
        Cntdr=0
        #se le pide al useario entrar la clave de la cancion
        NombreCancion=input('Ingrese el nombre de la cancion a tocar:')
        # este for busca toma la clave y la compara con las claves del dict
        for song in DictCanciones:
            #sie encuentra una clave entra a este condicional
            if NombreCancion==song:
                Cntdr=0
                print(f'Reproducuiendo >>>> {Dict[song]}')
            else:
                Cntdr+=1
        #si termina la busqueda y no encuentra nada imprime este mensaje
        if Cntdr==len(Dict):
            print("Cancion no encontrada")
        #con este input le permite seguir buscar mas canciones hasta que el user decida salir
        Msj=input("Desea buscar otra cancion y/n:")

BuscadorCanciones(DictCanciones)

