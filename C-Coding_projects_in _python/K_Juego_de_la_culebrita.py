import turtle as t
import random as r


t.bgcolor('crimson')

gusano=t.Turtle()
gusano.shape('square')
gusano.color('gold')
gusano.speed(0)
gusano.penup()
gusano.hideturtle()

gusano_2=t.Turtle()
gusano_2.shape('square')
gusano_2.color('aqua')
gusano_2.speed(0)
gusano_2.penup()
gusano_2.hideturtle()

hoja=t.Turtle()
forma_hoja= ((0, 0), (14, 2), (18, 6), (20, 20),(6, 18), (2, 14))
t.register_shape("hoja",forma_hoja)
hoja.shape('hoja')
hoja.color('green')
hoja.penup()
hoja.hideturtle()
hoja.speed(0)

comenzar_juego=False

texto=t.Turtle()
texto.write('Para empezar el juejo presiona espacio', align='center',
            font=('Arial',16,'bold'))

texto.hideturtle()

puntuacion=t.Turtle()
puntuacion.hideturtle()
puntuacion.speed(0)

puntuacion_2=t.Turtle()
puntuacion_2.hideturtle()
puntuacion_2.speed(0)




def afuera_de_la_ventana(gusano):
    lado_derecho=t.window_width()/2
    lado_izquierdo=-t.window_width()/2
    lado_arriba=t.window_height()/2
    lado_abajo=-t.window_height()/2

    (x,y)=gusano.pos()



    afuera= x>lado_derecho or x<lado_izquierdo or y>lado_arriba or y<lado_abajo

    return afuera


def fin_del_juego():
    gusano.color('crimson')
    gusano_2.color('crimson')
    hoja.color('crimson')
    t.penup()
    t.setpos(0,0)
    t.hideturtle()
    t.write("FIN DEL JUEGO",align='center',font=('Arial',25,'normal'))


def mostrar_puntuacion(puntuacion_actual_1,puntuacion_actual_2):
    puntuacion.clear()
    puntuacion.penup()
    puntuacion_2.clear()
    puntuacion_2.penup()

    x= (t.window_width()/2)-50
    y= (t.window_height()/2)-50

    puntuacion.setpos(x,y)
    puntuacion.write(str(puntuacion_actual_1),align='right',font=('Arial',10, 'bold'))

    x2 = (-t.window_width() / 2) + 50
    y2 = (t.window_height() / 2) - 50

    puntuacion_2.setpos(x2, y2)
    puntuacion_2.write(str(puntuacion_actual_2), align='right', font=('Arial', 10, 'bold'))


def colocar_hoja():
    hoja.ht()
    hoja.setx(r.randint(-200,200))
    hoja.sety(r.randint(-200,200))
    hoja.st()

def empezar_juego():
    global comenzar_juego

    if comenzar_juego:
        return

    comenzar_juego=True

    puntuacion=0
    puntuacion_2=0
    texto.clear()

    velocidad_gusano=3
    largo_gusano=3
    gusano.shapesize(1,largo_gusano,1)
    gusano.showturtle()
    mostrar_puntuacion(puntuacion,puntuacion_2)

    gusano_2.shapesize(1, largo_gusano, 1)
    gusano_2.setheading(180)
    gusano_2.showturtle()

    colocar_hoja()

    while True:
        gusano.fd(velocidad_gusano)
        gusano_2.fd(velocidad_gusano)

        if gusano.distance(hoja)<20:
            colocar_hoja()
            largo_gusano+=1
            gusano.shapesize(1,largo_gusano,1)
            velocidad_gusano+=1
            puntuacion+=5
            mostrar_puntuacion(puntuacion,puntuacion_2)
        elif gusano_2.distance(hoja)<20:
            colocar_hoja()
            largo_gusano+=1
            gusano_2.shapesize(1, largo_gusano, 1)
            velocidad_gusano+=1
            puntuacion_2+=5
            mostrar_puntuacion(puntuacion,puntuacion_2)

        if afuera_de_la_ventana(gusano) or afuera_de_la_ventana(gusano_2):
            if puntuacion>puntuacion_2:
                t.penup()
                t.setpos(0,100)
                t.write('Amarillo ha ganado' , align='center',
                        font=('Arial', 10, 'normal'))
                fin_del_juego()
            elif puntuacion < puntuacion_2:
                t.penup()
                t.setpos(0, 100)
                t.write('Azul ha ganado', align='center',
                        font=('Arial', 10, 'normal'))
                fin_del_juego()
            elif puntuacion == puntuacion_2:
                t.penup()
                t.setpos(0, 100)
                t.write('Empate', align='center',
                        font=('Arial', 10, 'normal'))
                fin_del_juego()
            else:
                fin_del_juego()
            break

def mover_arriba():
    if gusano.heading()==0 or gusano.heading()==180:
        gusano.setheading(90)
def mover_abajo():
    if gusano.heading()==0 or gusano.heading()==180:
        gusano.setheading(270)
def mover_derecha():
    if gusano.heading()==90 or gusano.heading()==270:
        gusano.setheading(0)
def mover_izquierda():
    if gusano.heading()==90 or gusano.heading()==270:
        gusano.setheading(180)

def mover_arriba_2():
    if gusano_2.heading()==0 or gusano_2.heading()==180:
        gusano_2.setheading(90)
def mover_abajo_2():
    if gusano_2.heading()==0 or gusano_2.heading()==180:
        gusano_2.setheading(270)
def mover_derecha_2():
    if gusano_2.heading()==90 or gusano_2.heading()==270:
        gusano_2.setheading(0)
def mover_izquierda_2():
    if gusano_2.heading()==90 or gusano_2.heading()==270:
        gusano_2.setheading(180)



t.onkey(empezar_juego,'space')

t.onkey(mover_arriba,'Up')
t.onkey(mover_abajo,'Down')
t.onkey(mover_derecha,'Right')
t.onkey(mover_izquierda,'Left')

t.onkey(mover_arriba_2,'w')
t.onkey(mover_abajo_2,'s')
t.onkey(mover_derecha_2,'d')
t.onkey(mover_izquierda_2,'a')


t.listen()
t.mainloop()
