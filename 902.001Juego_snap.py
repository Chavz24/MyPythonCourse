from tkinter import Canvas, Tk, HIDDEN, NORMAL
import time
import random


# esta funcion llama las fuguras de una en una mientras queden figuras en la lista
def siguiente_figura():
    global figura
    global color_anterior
    global color_actual
    color_anterior = color_actual
    v.delete(figura)
    if len(figuras) > 0:
        figura = figuras.pop()
        v.itemconfigure(figura, state=NORMAL)
        color_anterior = v.itemcget(figura, 'fill')
        raiz.after(1000, siguiente_figura)

    # cuando no hay mas figuras en la lista blockea las letras e imprime un mensaje diciendo cual es el ganador
    else:
        v.unbind('q')
        v.unbind('p')
        if puntuacion_jugador_1 > puntuacion_jugador_2:
            v.create_text(200, 200, text='Jugador 1 gana')
        elif puntuacion_jugador_2 > puntuacion_jugador_1:
            v.create_text(200, 200, text='Jeagador 2 gana')
        else:
            v.create_text(200, 200, text='Empate')

        v.pack()


# esta funcion detecta cuando los jugadores presoanan las teclas y asigna la puntuacion
def snap(event):
    global figura
    global puntuacion_jugador_1
    global puntuacion_jugador_2
    valido = False

    v.delete(figura)

    if color_anterior == color_actual:
        valido = True
    if valido:
        if event.char == 'q':
            puntuacion_jugador_1 += 1
        else:
            puntuacion_jugador_2 += 1
        figura = v.create_text(200, 200, text="SNAP, tienes un punto")
    else:
        if event.char == 'q':
            puntuacion_jugador_1 -= 1
        else:
            puntuacion_jugador_2 -= 1
        figura = v.create_text(200, 200, text="Fallaste, Punto menos")

    v.pack()

    raiz.update_idletasks()
    time.sleep(2)


raiz = Tk()

raiz.title('Snap')

v = Canvas(raiz, width=400, height=400)

figuras = []

circulo = v.create_oval(35, 26, 365, 350, outline='crimson', fill='crimson', state=HIDDEN)
figuras.append(circulo)
circulo = v.create_oval(35, 20, 365, 350, outline='green', fill='green', state=HIDDEN)
figuras.append(circulo)
circulo = v.create_oval(35, 26, 365, 350, outline='blue', fill='blue', state=HIDDEN)
figuras.append(circulo)
circulo = v.create_oval(35, 20, 365, 350, outline='pink', fill='pink', state=HIDDEN)
figuras.append(circulo)

Rectangulo = v.create_rectangle(35, 100, 365, 270, outline='crimson', fill='crimson', state=HIDDEN)
figuras.append(Rectangulo)
Rectangulo = v.create_rectangle(35, 100, 365, 270, outline='green', fill='green', state=HIDDEN)
figuras.append(Rectangulo)
Rectangulo = v.create_rectangle(35, 100, 365, 270, outline='blue', fill='blue', state=HIDDEN)
figuras.append(Rectangulo)
Rectangulo = v.create_rectangle(35, 100, 365, 270, outline='pink', fill='pink', state=HIDDEN)
figuras.append(Rectangulo)

v.pack()

# intercambia el orden de las figuras en la lista
random.shuffle(figuras)

figura = None
color_anterior = ''
color_actual = ''
puntuacion_jugador_1 = 0
puntuacion_jugador_2 = 0

raiz.after(3000, siguiente_figura)

v.bind('q', snap)
v.bind('p', snap)
v.focus_set()

raiz.mainloop()

