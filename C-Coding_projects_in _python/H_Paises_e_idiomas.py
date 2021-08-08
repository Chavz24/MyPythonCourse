import tkinter as tk
import tkinter.simpledialog
import tkinter.messagebox

print('Idimoas de paises')

raiz = tk.Tk()

raiz.withdraw()

paises_del_mundo = {}


# funcion para leer el archivo y crear un diccionario
def leer_archivo():
    with open('paises_por_idiomas.txt') as archivo:
        for linea in archivo:
            linea = linea.strip('\n')
            pais, idioma = linea.split('/')
            paises_del_mundo[pais] = idioma


# funcion para agregar paises a la lista
def agregar_paises_idomas(nombre_pais, idioma_pais):
    with open('paises_por_idiomas.txt', 'a') as archivo:
        archivo.write('\n' + nombre_pais + '/' + idioma_pais)


leer_archivo()

while True:
    # tk.simpledialog.askstring permite crar una ventana que le pide al usuari ingresar el pais
    pais_buscado = tk.simpledialog.askstring('Pais', 'Escribe el nombre del pais      ')
    pais_buscado = pais_buscado.capitalize()
    if pais_buscado in paises_del_mundo:
        respuesta = paises_del_mundo[pais_buscado]
        # tk.messagebox.showinfo muestra la respuesta en otra ventana
        tk.messagebox.showinfo('Respuesta', 'El idioma de ' + pais_buscado + ' es ' + respuesta)

    # en caso que el pais ingresado no es encuentre en la lista, el programa pide al
    # que ingrese su idioma y mediante la funcion agregar_paises_idomas lo agraga a la lista.
    else:
        nuevo_idioma = tk.simpledialog.askstring('Dime el idioma', 'No se el idioma de ' + pais_buscado +
                                                 '. Me lo dices, por favor?')

        tk.messagebox.showinfo('', 'Gracias')
        nuevo_idioma = nuevo_idioma.capitalize()
        paises_del_mundo[pais_buscado] = nuevo_idioma
        agregar_paises_idomas(pais_buscado, nuevo_idioma)

    raiz.mainloop()


