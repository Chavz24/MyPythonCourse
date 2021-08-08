import  turtle as t
import random as r
import itertools as h





radio=r.randint(1,100)
print(radio)

lista_colores=h.cycle(['aqua','palegreen','steelblue','crimson','violet','yellow','gold','lavender','plum'
               ,'darkgreen','cyan','coral','turquoise','blueviolet','lime','salmon'])


t.hideturtle()

def patron_circulos():
    t.speed(20)
    t.pensize(2)
    t.bgcolor('black')
    t.color(next(lista_colores))
    radio = r.randint(1, 100)
    movimiento_adelante=r.randint(1,10)
    movimiento_atras=r.randint(5,15)
    print(radio)
    t.circle(radio)
    for i in range(4):
        t.forward(radio)
        t.left(90)
    t.forward(movimiento_adelante)
    t.back(movimiento_atras)
    t.left(3)
    t.right(10)
    patron_circulos()
patron_circulos()