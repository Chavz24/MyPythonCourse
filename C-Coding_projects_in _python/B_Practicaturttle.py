import  turtle as t


def retangulo(horizontal,vertical, color):
    t.shape("turtle")
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    t.pd()
    for line in  range(1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()
while True:
    t.speed('normal')

    t.screensize(2500,1000)


    #feet
    t.pu()
    t.goto(-100,-50)
    retangulo(50,25,'dodger blue')
    t.goto(150,-50)
    retangulo(50,25,'blue')

    #legs
    t.goto(-85,50)
    retangulo(25,100,'red')
    t.goto(165,50)
    retangulo(25,100,'red')

    #body
    t.goto(-70,200)
    retangulo(250,150,'orange')

    #arms
    #upper arms

    t.goto(-95,200)
    retangulo(25,70,'red')
    t.goto(180,200)
    retangulo(25,70,'red')

    #lower arms
    t.goto(180,130)
    retangulo(70,20,'black')
    t.goto(-140,130)
    retangulo(70,20,'black')

    #neck
    t.goto(5,230)
    retangulo(100,30,'brown')

    #head
    t.goto(30,270)
    retangulo(50,40,'purple')


