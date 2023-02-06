import turtle

def drawsquare (zaki, size):
    for i in range(4):
        zaki.forward(size)
        zaki.left(90)


def main ():
    wn = turtle.Screen()
    wn.bgcolor("gray")
    zaki = turtle.Turtle()
    zaki.fillcolor("White")
    zaki.hideturtle()
    zaki.speed(0)
    zaki.penup()
    zaki.setpos(-220, 100)
    zaki.pendown()

    for i in range(8):
        if (i) % 2 == 0:
            zaki.fillcolor("white")
        else:
            zaki.fillcolor("black")
        zaki.begin_fill()
        drawsquare(zaki, 60)
        zaki.forward(60)
        zaki.end_fill()


    zaki.penup()
    zaki.setpos(-220, 40)
    zaki.pendown()
    for i in range(8):
        if (i) % 2 == 0:
            zaki.fillcolor("black")
        else:
            zaki.fillcolor("white")
        zaki.begin_fill()
        drawsquare(zaki, 60)
        zaki.forward(60)
        zaki.end_fill()

    zaki.penup()
    zaki.setpos(-220, -20)
    zaki.pendown()
    for i in range(8):
        if (i) % 2 == 0:
            zaki.fillcolor("white")
        else:
            zaki.fillcolor("black")
        zaki.begin_fill()
        drawsquare(zaki, 60)
        zaki.forward(60)
        zaki.end_fill()

    zaki.penup()
    zaki.setpos(-220, -80)
    zaki.pendown()
    for i in range(8):
        if (i) % 2 == 0:
            zaki.fillcolor("black")
        else:
            zaki.fillcolor("white")
        zaki.begin_fill()
        drawsquare(zaki, 60)
        zaki.forward(60)
        zaki.end_fill()

    zaki.penup()
    zaki.setpos(-220, -140)
    zaki.pendown()
    for i in range(8):
        if (i) % 2 == 0:
            zaki.fillcolor("white")
        else:
            zaki.fillcolor("black")
        zaki.begin_fill()
        drawsquare(zaki, 60)
        zaki.forward(60)
        zaki.end_fill()

    zaki.penup()
    zaki.setpos(-220, -200)
    zaki.pendown()
    for i in range(8):
        if (i) % 2 == 0:
            zaki.fillcolor("black")
        else:
            zaki.fillcolor("white")
        zaki.begin_fill()
        drawsquare(zaki, 60)
        zaki.forward(60)
        zaki.end_fill()

    zaki.penup()
    zaki.setpos(-220, -260)
    zaki.pendown()
    for i in range(8):
        if (i) % 2 == 0:
            zaki.fillcolor("white")
        else:
            zaki.fillcolor("black")
        zaki.begin_fill()
        drawsquare(zaki, 60)
        zaki.forward(60)
        zaki.end_fill()

    zaki.penup()
    zaki.setpos(-220, -320)
    zaki.pendown()
    for i in range(8):
        if (i) % 2 == 0:
            zaki.fillcolor("black")
        else:
            zaki.fillcolor("white")
        zaki.begin_fill()
        drawsquare(zaki, 60)
        zaki.forward(60)
        zaki.end_fill()
    wn.exitonclick()

main()

