import tkinter as tk
from  tkinter import  simpledialog
from  tkinter import  messagebox
from random import choice

#eesta funcion le pregunta al usuario lo que desea realizar
def tarea_a_realizar():
    tarea= tk.simpledialog.askstring('Tarea','Que tarea quiere realizar, encriptar o desencriptar?')
    tarea= tarea.lower()
    return tarea
#eesta funcion le pide el mensaje sobre el cual se va a realizar la accion deseada
def mensaje_secreto():
    mensaje=tk.simpledialog.askstring('','Ingrese el mensaje aqui: ')
    return mensaje
# esta funcion devuelve True si el mensaje tiene un numero par de letras False de lo contrario
def caracter_par_o_impar(numero_caracteres):
    return numero_caracteres%2==0
#Hece una lista con los caracteres pares
def caracteres_pares(mensaje):
    lista_caraters_pares=[]
    for caracter in range(0,len(mensaje)):
        if caracter_par_o_impar(caracter):
            lista_caraters_pares.append(mensaje[caracter])
    return lista_caraters_pares
#Hece una lista con los caracteres impares
def caracteres_impares(mensaje):
    lista_caraters_impares=[]
    for caracter in range(0,len(mensaje)):
        if caracter_par_o_impar(caracter)==False:
            lista_caraters_impares.append(mensaje[caracter])
    return lista_caraters_impares
#intercambia la posicion de los carateres
def intercambiar_posicion_caracteeres(mensaje):
    lista_cracteres=[]
    if caracter_par_o_impar(len(mensaje)):
        mensaje=mensaje+'X'
    caracter_pares= caracteres_pares(mensaje)
    caracter_impares= caracteres_impares(mensaje)
    #el mensaje se divide entre dos por que la condicion se arriba lo hace siempre par y de est manera no tira error
    # ya que las listas de numenos pares e impares solo tienen la mitad de los caracteres del mensaje orignal
    for caracter in range (0,int(len(mensaje)/2)):
        lista_cracteres.append(caracter_pares[caracter])
        lista_cracteres.append(caracter_impares[caracter])
    mensaje_nuevo=''.join(lista_cracteres)
    return mensaje_nuevo
# esta funcion encripta el mensaje en tres capas: la primera usa la funcion anterior,
#la segunda une los caracteres comenzando desde el ultimo
#la tercera inserta caracteres falsos aleatorios en las posiciones impares.
def mensaje_encriptado(mensaje):
    caracteres_falsos=['T','A']
    encriptar_nivel_3 = []

    encriptado_nivel_1=intercambiar_posicion_caracteeres(mensaje)
    encriptado_nivel_2=''.join(reversed(encriptado_nivel_1))
    for caracter in range (0,len(encriptado_nivel_2)):
        encriptar_nivel_3.append(encriptado_nivel_2[caracter])
        encriptar_nivel_3.append(choice(caracteres_falsos))
    encriptado_nivel_3=''.join(encriptar_nivel_3)

    return encriptado_nivel_3
# esta funcion desencripta el mensaje empezando por en orden inverso que la anterior funcion
def mensaje_desencriptado(mensaje):
    desencriptado_mensaje_nivel_1=caracteres_pares(mensaje)
    desencriptado_mensaje_nivel_2=''.join(reversed(desencriptado_mensaje_nivel_1))
    desencriptado_mensaje_nivel_3=intercambiar_posicion_caracteeres(desencriptado_mensaje_nivel_2)
    return desencriptado_mensaje_nivel_3

raiz=tk.Tk()

raiz.withdraw()

#aqui empieza el loop del programa
while True:
    #tarea a realizar:encriptar o desencriptar
    tarea=tarea_a_realizar()

    if tarea=='encriptar':
        mensaje=mensaje_secreto()
        msj_encriptado= mensaje_encriptado(mensaje)
        print(msj_encriptado)
        tk.messagebox.showinfo('','El mensaje  encriptado es: '+ msj_encriptado)
    elif tarea=='desencriptar':
        mensaje=mensaje_secreto()
        msj_desencriptado = mensaje_desencriptado(mensaje)
        tk.messagebox.showinfo('','El mensaje a desencriptar es: ' + msj_desencriptado)
    else:
        tk.messagebox.showerror('','Funcion no reconocida')
        break
raiz.mainloop()