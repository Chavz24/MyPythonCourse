import tkinter as tk
import datetime as dt


# esta funcio recorre el archivo y extrae los datos
def extraer_eventos():
    # aqui se almacenan los datos
    lista_eventos = []
    ##abro el archivo
    with open('events.txt') as archivo:
        # uso un bucle for para recorrer el archivo
        for linea in archivo:
            # uso esto porque al final del bucle se me imprime una lista vacia,**no se por que
            # para evitar que esto pase uso un condicional para romper el bucle antes de que se guarde en
            # la lista vacia se guarde en la lista 'eventos'
            if linea != '\n':
                # remuevo todas las lineas en el archivo
                linea = linea.strip('\n')
                # divido el evento en dos, un nombre y su fecha correspondiente
                evento_actual = linea.split(',')
                # convieto a formato fecha la fecha del evento, esto le quita las horas, minutos y segundos
                fecha_evento = dt.datetime.strptime(evento_actual[1], '%d/%m/%Y').date()
                # guardo la fecha en formarto fecha en la lista evento_actual
                evento_actual[1] = fecha_evento
                # guardo cada evento en la lista_eventos
                lista_eventos.append(evento_actual)
            else:
                break
    # la funcion retorna la lista de eventos
    return lista_eventos


# esta funcion regresa los dias que faltan para el evento.
def dias_faltantes(fecha_de_evento, fecha_hoy):
    # sta linea resta la fecha del evento con la fecha actual y convierte el resultado a cadena
    tiempo_restante_para_evento = str(evento[1] - hoy)
    # esto crea una lista con los dias, horas, etc
    numero_dias = tiempo_restante_para_evento.split(' ')
    # como a mi solo me interesan los dias la funcion retorna solo ese valor
    return numero_dias[0]


# creo una GUI
raiz = tk.Tk()

# dimenciones y otras caracteristicas del la ventana
ventana = tk.Canvas(raiz, width=600, height=500, bg='black')
ventana.pack()
ventana.create_text(40, 10, anchor='nw', fill='aqua',
                    font='arial 30 ', text='Lista de eventos')

# aqui llamo a la funcion para que me de todos los eventos de lista_eventos
eventos = extraer_eventos()
# asigno una la fecha de hoy a una variable
hoy = dt.date.today()
# uso este espaciad_vertical para separar las lineas de los evntos
espaciado_vertical = 60

# con este bucle for recorro cada evento en eventos para separarlos del nombre y la fecha
for evento in eventos:
    # separo el nombre
    nombre_evento = evento[0]
    # con las funcion hace el trabajo de darme los dias que faltan has el evento, solo tenho que darle
    # los parametros
    dias_hasta_evento = dias_faltantes(evento[1], hoy)
    # estee condicional cambia el color de las letras si el dia del evento esta a 10 o menos dias de ocurrir
    if int(dias_hasta_evento) <= 10:
        color_letra = 'red'
    else:
        color_letra = 'blueviolet'

    # esto imprime los datos en el GUI.
    lista = '>>>>Faltan %s para %s' % (dias_hasta_evento, nombre_evento)
    ventana.create_text(25, espaciado_vertical, anchor='w', fill=color_letra,
                        font='arial 10 bold ', text=lista)
    # aumenta el espacio entre lineas para evitar que se impriman todos encima de todos
    espaciado_vertical += 20

raiz.mainloop()
